# PHANToM Grid :: Tournament Brief & Dual-Track Staging Plan
> **Tournament**: QNX Global Hackathon 2026  
> **Prize Pool**: $50,000 USD  
> **Deadline**: December 15, 2026 @ 2:00 PM ET (Taipei: Dec 16, 03:00 AM)  
> **Status**: STAGED & REGISTERING

---

## 1. Core Thesis
Demonstrate **PHANToM Grid Automotive ASIL-D Embedded Motion & Thermal Damping Engine on QNX RTOS**:
- **Vehicle Interface**: Automotive CAN-FD 64B & ADC chassis telemetry integration.
- **Motor Control Core**: PG-MOD-29-MOTOR PMSM FOC vector control, Clarke/Park transform (<= 1.85us), and 1.35x torque thermal damping.
- **Microkernel Determinism**: QNX hard real-time POSIX scheduling compliance with 2-Pass ZDR (0.00MB residual).

---

## 2. Standard 10-Drawer Mapping Plan
1. `01_Specs`: Automotive ASIL-D whitepaper with 4 diagrams and 1 table.
2. `02_Architecture`: QNX RTOS microkernel thread topology and FOC state machine.
3. `03_Source_Code`: C++/Rust QNX motor control pipeline.
4. `04_Slides_PDF`: Official Tournament Deck.
5. `05_DemoVideo_1440P`: 1440P 60FPS Hollywood presentation.
6. `06_Test_Reports`: QNX latency benchmarks and pure ASCII test reports.
7. `07_Submission`: Devpost markdown copy and pitch strings.
8. `08_Audit_WORM`: Cryptographic receipts and 2-Pass ZDR verification.
9. `09_Assets`: 16:9 Cover image and telemetry HUD assets.
10. `10_Releases`: GitHub release zip and tag references.
