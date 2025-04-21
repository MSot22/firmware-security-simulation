import csv
import os

def sign_payload(payload):
    secret_key = "abc123"
    return hash(payload + secret_key)

def verify_signature(firmware):
    if firmware.get('signature') is None:
        return False
    expected = sign_payload(firmware['payload'])
    return firmware['signature'] == expected

def log_results(filename, label, time_taken, success):
    file_exists = os.path.isfile(filename)
    with open(filename, 'a', newline='') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["Label", "Time (s)", "Success"])
        writer.writerow([label, f"{time_taken:.6f}", success])
