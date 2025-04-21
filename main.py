from device import Device
from firmware import generate_valid_firmware
from attacker import craft_unsigned_firmware
from utils import log_results

if __name__ == "__main__":
    results_file = "test_results.csv"

    device_secure = Device(secure_boot=True)
    device_insecure = Device(secure_boot=False)

    print("\n[Test 1] Valid signed firmware on secure device:")
    firmware_valid = generate_valid_firmware("2.0", "safe_code")
    time1, result1 = device_secure.update_firmware(firmware_valid)
    log_results(results_file, "Valid Firmware", time1, result1)

    print("\n[Test 2] Malicious unsigned firmware on secure device:")
    firmware_bad = craft_unsigned_firmware()
    time2, result2 = device_secure.update_firmware(firmware_bad)
    log_results(results_file, "Unsigned Firmware (Secure Boot)", time2, result2)

    print("\n[Test 3] Malicious unsigned firmware on insecure device:")
    time3, result3 = device_insecure.update_firmware(firmware_bad)
    log_results(results_file, "Unsigned Firmware (No Secure Boot)", time3, result3)

    print("\n[Done] All results saved to test_results.csv.")
