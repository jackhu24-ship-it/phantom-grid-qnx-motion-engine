# 03_Source_Code // Build and Run Instructions

- **Target OS**: QNX SDP 8.0 (QNX Neutrino RTOS)
- **Target Environment**: QNX 8.0 x86_64 / AArch64 target hardware or QEMU virtual target (plus host-side verification environment)
- **Toolchain**: QNX 8.0 `qcc` / `aarch64-unknown-nto-qnx8.0.0-gcc` or `x86_64-pc-nto-qnx8.0.0-gcc`, and Python 3.10+ for telemetry/simulation harnesses

## 1. Run Motion & Thermal Damping Kernel Simulation / Verification
```bash
python3 qnx_motion_kernel.py --cycles 100 --test-overload --json
```

## 2. Run Unit Closure & Chaos Tests
```bash
python3 test_closure.py
```

## 3. Build & Run Native C++ Kernel
```bash
make
./qnx_motion_kernel
```

## 4. QNX SDP 8.0 Cross-Compilation & QEMU Target Deployment
```bash
chmod +x run_qnx_qemu.sh
./run_qnx_qemu.sh
```
