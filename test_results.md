# Firmware Security Simulation Results

| Test Case                               | Time (s) | Success |
|----------------------------------------|----------|---------|
| Valid Firmware                      | 0.00003  | True    |
| Unsigned Firmware (Secure Boot)     | 0.00004  | False   |
| Unsigned Firmware (No Secure Boot) | 0.00001  | True    |

> This table summarizes the results of the firmware update simulation. 
> Only signed firmware was accepted by devices with secure boot enabled. 
> Unsigned firmware was rejected by secure devices, but accepted when secure boot was off.
