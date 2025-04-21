from firmware import Firmware

class UpdateManager:
    def __init__(self):
        pass

    def generate_valid_firmware(self, version, payload):
        return Firmware(version=version, payload=payload, signed=True)
