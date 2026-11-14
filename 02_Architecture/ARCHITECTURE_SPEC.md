# PHANToM GRID :: QNX Microkernel Thread Topology & Architecture
> QNX Neutrino RTOS Real-Time System Engineering Specification

---

## 1. Thread Hierarchy & Priorities
- **Thread 0 (Priority 63, SCHED_FIFO)**: Hard Real-Time Motor Control Loop (FOC Clarke/Park transforms).
- **Thread 1 (Priority 60, SCHED_FIFO)**: High-Speed CAN-FD 64B Pulse Receiver & Parser.
- **Thread 2 (Priority 58, SCHED_RR)**: 1.35x Thermal Damping Watchdog & Stator Temperature Observer.
- **Thread 3 (Priority 20, SCHED_OTHER)**: Telemetry Exporter & Live HUD Streaming.
- **Thread 4 (Priority 10, SCHED_OTHER)**: 2-Pass ZDR Memory Shredder & Diagnostic Logger.

---

## 2. Priority Inversion Defense
In accordance with QNX Neutrino microkernel best practices, all mutexes deployed in shared state buffer channels use priority inheritance (`PTHREAD_PRIO_INHERIT`) to avoid unbounded priority inversions during burst periods.
