# Firmware Security Simulation

## Project Title:
**Evaluating the Role of Firmware Signing and Secure Boot in Reducing Firmware Tampering Exposure in IoT Smart Home Systems**

## 1. Introduction
This project simulates a smart home hub device's firmware update mechanism, investigating whether firmware signing and secure boot features can reduce system exposure to unauthorized or malicious firmware updates. 

## 2. Hypothesis
“Can implementing firmware signing and secure boot in an IoT smart home hub reduce exposure to unauthorized firmware tampering without significantly impacting system performance?”

## 3. Implementation Overview

### Core Components
- **Device Class**: Represents the smart home device with an optional secure boot feature.
- **Firmware Object**: A dictionary simulating firmware data, version, and signature.
- **Update Manager**: Sends legitimate, signed firmware to the device.
- **Attacker Simulation**: Sends unsigned/malicious firmware.
- **Utility Functions**: Used to generate and verify digital signatures (simulated using hashing).

### How It Works
The simulation tests three scenarios:
1. A secure device receives valid signed firmware.
2. A secure device receives unsigned malicious firmware.
3. A device without secure boot receives malicious firmware.

The simulation logs whether the update was accepted and the time taken, simulating a performance check.

## 4. How to Run the Simulation

### Prerequisites
- Python 3.x (recommended: 3.8+)
- No external libraries required

### Steps
1. Open a terminal in the folder containing `firmware_sim.py`.
2. Run the script:
```bash
python firmware_sim.py
```
3. Output will be printed to the console, and results saved to `test_results.csv`.

### Output Example
```
[Test 1] Valid signed firmware on secure device:
[+] Firmware updated to version 2.0

[Test 2] Malicious unsigned firmware on secure device:
[!] Firmware rejected: Invalid or unsigned.

[Test 3] Malicious unsigned firmware on insecure device:
[+] Firmware updated to version X.666
```

## 5. Analysis and Discussion

### Results Summary (from test_results.csv):
- Valid signed firmware updates succeeded.
- Unsigned updates were rejected only when secure boot was enabled.
- Minimal time overhead for signature verification (~0.00004s).

### Discussion:
These results validate the hypothesis: firmware signing and secure boot effectively block firmware tampering, significantly reducing exposure. There is no meaningful impact on performance, even in a simulated resource-constrained environment. However, without enforcing secure boot, the system is easily compromised, showing the importance of this feature in IoT device security.

## 6. References
- OWASP Foundation. (2018). OWASP IoT Top 10.
- FIRST.org. (2019). CVSS v3.1 Specification.
- MITRE Corporation. (2023). MITRE ATT&CK Framework.
- Hernan, S. et al. (2006). STRIDE Threat Modelling.
- Kodali, R.K. et al. (2016). IoT Based Smart Home Security System.

---

## Author Note
This simulation is intended for academic demonstration and simplifies real-world firmware validation. Production-level secure boot should use cryptographic signatures validated by hardware-based root of trust.

