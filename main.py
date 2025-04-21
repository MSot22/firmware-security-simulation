import csv
import time
from device import Device
from update_manager import UpdateManager
from attackers import Attacker

def log_results(filename, label, time_taken, success):
    with open(filename, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([label, f"{time_taken:.5f}", success])

if __name__ == "__main__":
    device = Device(secure_boot=True)
    updater = UpdateManager()
    attacker = Attacker()

    print("\n[TEST 1] Applying valid firmware...")
    firmware = updater.generate_valid_firmware("2.0", "safe_payload")
    duration, result = device.update_firmware(firmware)
    log_results("test_results.csv", "Valid Firmware", duration, result)

    print("\n[TEST 2] Attacker sends unsigned firmware...")
    fake_firmware = attacker.craft_unsigned_firmware()
    duration, result = device.update_firmware(fake_firmware)
    log_results("test_results.csv", "Malicious Firmware", duration, result)

    print("\n[TEST 3] Disabling secure boot (insecure device)...")
    device_insecure = Device(secure_boot=False)
    duration, result = device_insecure.update_firmware(fake_firmware)
    log_results("test_results.csv", "Unsigned Firmware (No Secure Boot)", duration, result)
