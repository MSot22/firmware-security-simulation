from utils import verify_signature

class Device:
    def __init__(self, secure_boot=True):
        self.secure_boot = secure_boot
        self.current_version = "1.0"

    def update_firmware(self, firmware):
        from time import time
        start = time()
        if self.secure_boot and not verify_signature(firmware):
            print("[!] Firmware rejected: Invalid or unsigned.")
            return time() - start, False
        self.current_version = firmware['version']
        print(f"[+] Firmware updated to version {firmware['version']}")
        return time() - start, True
