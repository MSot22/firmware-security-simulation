import time
import csv
import os

# --------------------------------------------
# Utility Functions: Signing and Verification
# --------------------------------------------

def sign_payload(payload):
    """
    Simulates digital signature creation using a secret key and hash.
    """
    secret_key = "abc123"
    return hash(payload + secret_key)


def verify_signature(firmware):
    """
    Verifies if the firmware signature matches the expected signature.
    """
    if firmware.get('signature') is None:
        return False
    expected_signature = sign_payload(firmware['payload'])
    return firmware['signature'] == expected_signature

# --------------------------------------------
# Device Class
# --------------------------------------------

class Device:
    """
    Represents an IoT hub with secure boot capability.
    """
    def __init__(self, secure_boot=True):
        self.secure_boot = secure_boot
        self.current_version = "1.0"

    def update_firmware(self, firmware):
        """
        Attempts to update firmware, checking signature if secure boot is enabled.
        Returns time taken and success status.
        """
        start = time.time()
        if self.secure_boot and not verify_signature(firmware):
            print("[!] Firmware rejected: Invalid or unsigned.")
            return time.time() - start, False

        self.current_version = firmware['version']
        print(f"[+] Firmware updated to version {firmware['version']}")
        return time.time() - start, True

# --------------------------------------------
# Firmware Creators
# --------------------------------------------

def generate_valid_firmware(version, payload):
    """
    Creates a signed, valid firmware update.
    """
    return {
        'version': version,
        'payload': payload,
        'signature': sign_payload(payload)
    }


def craft_unsigned_firmware():
    """
    Creates a malicious firmware without a signature.
    """
    return {
        'version': 'X.666',
        'payload': 'malicious_code',
        'signature': None
    }

# --------------------------------------------
# Logging Results
# --------------------------------------------

def log_results(filename, label, time_taken, success):
    """
    Writes results to a CSV file.
    """
    file_exists = os.path.isfile(filename)
    with open(filename, 'a', newline='') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["Label", "Time (s)", "Success"])
        writer.writerow([label, f"{time_taken:.6f}", success])

# --------------------------------------------
# Main Simulation
# --------------------------------------------

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
