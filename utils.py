def sign_payload(payload):
    secret_key = "abc123"
    return hash(payload + secret_key)

def verify_signature(firmware):
    if firmware.signature is None:
        return False
    expected = sign_payload(firmware.payload)
    return firmware.signature == expected
