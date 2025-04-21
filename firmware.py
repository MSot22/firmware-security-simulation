import time
import csv
import os

# --- Utility Functions ---

def sign_payload(payload):
    secret_key = "abc123"
    return hash(payload + secret_key)

def verify_signature(firmware):
    if firmware['signature'] is None:
        return False
    expected = sign_payload(firmware['payload'])
    return firmware['signature'] == expected

# --- Device Class ---
class Device:
    def __init__(self, secure_boot=True):
        self.current_version = "1.0"
        self.secure_boot = secure_boot

    def update_firmware(self, firmware):
        start = time.time()
        if self.secure_boot and not verify_signature(firmware):
            print("[!] Firmware rejected: Invalid or unsigned.")
            return time.time() - start, False

        self.current_version = firmware['version']
        print(f"[+] Firmware updated to version {firmware['version']}")
        return time.time() - start, True

# --- UpdateManager ---
def generate_valid_firmware(version, payload):
    return {
        'version': version,
        'payload': payload,
        'signature': sign_payload(payload)
    }

# --- Attacker ---
def craft_unsigned_firmware():
    return {
        'version': 'X.666',
        'payload': 'malicious_code',
        'signature': None
    }

# --- Logging ---
def log_results(filename, label, time_taken, success):
    if not os.path.exists(filename):
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Label", "Time (s)", "Success"])
    with open(filename, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([label, f"{time_taken:.6f}", success])

# --- Main Test Runner ---
if __name__ == "__main__":
    results_file = "test_results.csv"

    device_secure = Device(secure_boot=True)
    device_insecure = Device(secure_boot=False)

    print("\n[Test 1] Valid signed firmware on secure device:")
    fw_valid = generate_valid_firmware("2.0", "safe_code")
    t1, r1 = device_secure.update_firmware(fw_valid)
    log_results(results_file, "Valid Firmware", t1, r1)

    print("\n[Test 2] Malicious unsigned firmware on secure device:")
    fw_fake = craft_unsigned_firmware()
    t2, r2 = device_secure.update_firmware(fw_fake)
    log_results(results_file, "Unsigned Firmware (Secure Boot)", t2, r2)

    print("\n[Test 3] Malicious unsigned firmware on insecure device:")
    t3, r3 = device_insecure.update_firmware(fw_fake)
    log_results(results_file, "Unsigned Firmware (No Secure Boot)", t3, r3)

    print("\n[Done] Results written to test_results.csv")
