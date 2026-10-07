import hashlib
import secrets
from pathlib import Path

DEVICE_FILE = Path(__file__).resolve().parent.parent / ".device_id"

def get_device_id():
    if DEVICE_FILE.exists():
        return DEVICE_FILE.read_text().strip().upper()

    raw = secrets.token_hex(32)
    device_id = hashlib.sha256(raw.encode()).hexdigest()[:16].upper()

    DEVICE_FILE.write_text(device_id)
    return device_id
