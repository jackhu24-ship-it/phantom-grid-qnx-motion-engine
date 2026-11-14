#!/usr/bin/env python3
"""
Unit Closure & Chaos Verification Suite for QNX Motion Kernel
Gate-Before-Ship Compliance Check
"""

import sys
import os
import time
import math
import unittest

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from qnx_motion_kernel import (
    QNXMotionKernel,
    generate_mock_canfd_frame,
    THERMAL_DAMPING_FACTOR,
    MAX_SAFE_TORQUE_NM
)

class TestQNXMotionKernel(unittest.TestCase):
    def setUp(self):
        self.kernel = QNXMotionKernel()

    def test_clarke_park_math(self):
        # Balanced 3-phase currents: ia = 10, ib = -5, ic = -5
        ia, ib = 10.0, -5.0
        i_alpha, i_beta = self.kernel.clarke_transform(ia, ib)
        self.assertAlmostEqual(i_alpha, 10.0)
        self.assertAlmostEqual(i_beta, 0.0)

        # Park transform at theta = 0
        i_d, i_q = self.kernel.park_transform(i_alpha, i_beta, 0.0)
        self.assertAlmostEqual(i_d, 10.0)
        self.assertAlmostEqual(i_q, 0.0)

    def test_thermal_damping_ratio(self):
        # Nominal torque: 50 Nm -> no damping
        torque_nom, damped = self.kernel.apply_thermal_damping(50.0, 80.0)
        self.assertFalse(damped)
        self.assertEqual(torque_nom, 50.0)

        # Overload torque: 135 Nm -> exactly 1.35x damping -> 100 Nm
        torque_over, damped = self.kernel.apply_thermal_damping(135.0, 90.0)
        self.assertTrue(damped)
        self.assertAlmostEqual(torque_over, 100.0, places=4)

        # Thermal overload: 60 Nm at 120 deg C -> triggers damping
        torque_therm, damped = self.kernel.apply_thermal_damping(60.0, 120.0)
        self.assertTrue(damped)
        self.assertAlmostEqual(torque_therm, 60.0 / 1.35, places=4)

    def test_canfd_unpack(self):
        frame = generate_mock_canfd_frame(12.5, -6.25, 1.57, 75.0, 85.0)
        self.assertEqual(len(frame), 64)
        ia, ib, theta, torque, temp = self.kernel.decode_canfd_telemetry(frame)
        self.assertAlmostEqual(ia, 12.5, places=2)
        self.assertAlmostEqual(ib, -6.25, places=2)
        self.assertAlmostEqual(theta, 1.57, places=2)
        self.assertAlmostEqual(torque, 75.0, places=2)
        self.assertAlmostEqual(temp, 85.0, places=2)

    def test_zdr_residual_zero(self):
        residual = self.kernel.execute_2pass_zdr()
        self.assertEqual(residual, 0.00)
        self.assertEqual(self.kernel.vram_allocated_gb, 0.00)

    def test_1000_cycle_chaos(self):
        for i in range(1000):
            torque = 100.0 if (i % 2 == 0) else 40.0
            temp = 120.0 if (i % 5 == 0) else 65.0
            frame = generate_mock_canfd_frame(
                ia=10.0 * math.sin(i * 0.05),
                ib=10.0 * math.sin(i * 0.05 - 2.094),
                theta=(i * 0.02) % (2 * math.pi),
                torque=torque,
                temp=temp
            )
            state = self.kernel.step_control_loop(frame)
            self.assertLess(state.cycle_latency_us, 50.0, "Latency ceiling violated")
            if torque > MAX_SAFE_TORQUE_NM or temp > 115.0:
                self.assertTrue(state.damping_active)

        final_zdr = self.kernel.execute_2pass_zdr()
        self.assertEqual(final_zdr, 0.00)

if __name__ == "__main__":
    unittest.main()
