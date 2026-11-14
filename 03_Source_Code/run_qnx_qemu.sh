#!/usr/bin/env bash
# PHANToM GRID // QNX 8.0 SDP & QEMU Target Deployment Script
set -e

echo "=== PHANToM GRID // QNX SDP 8.0 Target Deployment ==="

# Check for QNX SDP environment
if [ -n "$QNX_TARGET" ]; then
    echo "[*] QNX SDP detected at: $QNX_TARGET"
    echo "[*] Cross-compiling using QNX qcc compiler..."
    qcc -Vgcc_ntox86_64 -O3 -o qnx_motion_kernel qnx_motion_kernel.cpp
    echo "[*] Ready to dispatch to QNX QEMU virtual machine or hardware target."
else
    echo "[*] Standard POSIX Host / QEMU User Emulation Mode"
    echo "[*] Compiling using native C++ toolchain..."
    make
    echo "[*] Executing real-time simulation test..."
    ./qnx_motion_kernel
fi

echo "=== Deployment & Verification Complete ==="
