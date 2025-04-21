import time
from .utils import verify_signature

class Device:
    def __init__(self, secure_boot=True):
        self.current_version = "1.0"
        self.secure_boot = secure_boot

    def update_firmware(self, firmware):
        start = time.time()
        if self.secure_boot:
            if not verify_signature(firmware):
                print("[!] Update rejected: Invalid signature.")
                return time.time() - start, False
        self.current_version = firmware.version
        print(f"[+] Firmware updated to version {firmware.version}")
        return time.time() - start, True
