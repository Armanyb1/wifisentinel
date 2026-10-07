from banner import BANNER
from device import get_device_id
from license import get_license

def main():
    print(BANNER)
    device_id = get_device_id()
    print(f"Device ID : {device_id}")

    license_info = get_license(device_id)

    if license_info:
        plan, expires_at = license_info
        print(f"License   : {plan}")
        print(f"Expires   : {expires_at or 'LIFETIME'}")
    else:
        print("License   : NOT ACTIVATED")
        print("Contact the administrator for activation.")

if __name__ == "__main__":
    main()
