import hashlib
import platform
import uuid

def get_device_id():
    raw = "|".join([
        platform.system(),
        platform.machine(),
        platform.release(),
        str(uuid.getnode()),
        "WiFiSentinel"
    ])
    return hashlib.sha256(raw.encode()).hexdigest()[:16].upper()
