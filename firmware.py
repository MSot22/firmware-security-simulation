from utils import sign_payload

def generate_valid_firmware(version, payload):
    return {
        'version': version,
        'payload': payload,
        'signature': sign_payload(payload)
    }
