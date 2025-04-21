from firmware import Firmware

class Attacker:
    def craft_unsigned_firmware(self):
        return Firmware(version="X.666", payload="malicious_code", signed=False)
