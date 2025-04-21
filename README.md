# Firmware Security Simulation

## Project Title
**Evaluating the Role of Firmware Signing and Secure Boot in Reducing Firmware Tampering Exposure in IoT Smart Home Systems**

---

## Project Overview
This Python-based simulation models how an IoT smart home device handles firmware updates under secure and insecure conditions. It demonstrates the role of:
- **Firmware signing** using a mock hashing method
- **Secure boot** to block unauthorized firmware

The goal is to test if these features reduce exposure to firmware tampering, a critical attack vector in IoT devices.

---

## Hypothesis
“Can implementing firmware signing and secure boot in an IoT smart home hub reduce exposure to unauthorized firmware tampering without significantly impacting system performance?”

---

## How It Works

### Components
- `Device`: Represents the IoT hub; can enable or disable secure boot.
- `Firmware`: Represents update packages (signed/unsigned).
- `Update Manager`: Sends signed, valid firmware.
- `Attacker`: Simulates a malicious unsigned update.
- `Utils`: Contains functions to sign, verify, and log results.

### Test Scenarios
| Test | Description | Expected Result |
|------|-------------|-----------------|
| T1 | Valid signed firmware on secure device | Success |
| T2 | Unsigned firmware on secure device | Rejected |
| T3 | Unsigned firmware on insecure device | Accepted (unsafe) |

---

## Running the Simulation

### Requirements
- Python 3.8+
- No extra libraries needed

### Steps
1. Open a terminal in the folder
2. Run the simulation:
   ```bash
   python main.py
   ```
3. View results in the generated file: `test_results.csv`

---

## File Structure

| File         | Description |
|--------------|-------------|
| `main.py`    | Runs all test cases |
| `device.py`  | Contains the IoT device logic |
| `firmware.py`| Creates valid signed firmware |
| `attacker.py`| Generates malicious unsigned firmware |
| `utils.py`   | Signing, verification, and logging functions |
| `test_results.csv` | Output log of each test scenario |

---

## Notes
- Signature verification is simulated using Python’s built-in `hash()`.
- Secure boot is modeled as a software toggle.
- Performance timing is used to measure latency for each update.

---

## References
- OWASP IoT Top 10 (2018)
- STRIDE Threat Modelling
- CVSS v3.1 by FIRST.org
- MITRE ATT&CK Framework
- Kordy et al. (2014) - Attack–Defense Trees

---

> For academic use only. This prototype is a simulation and does not implement real cryptographic protections.
