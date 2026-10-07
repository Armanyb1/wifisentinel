# WiFiSentinel

## Professional Wi-Fi Security & Assessment Toolkit

WiFiSentinel is a lightweight security-assessment and diagnostic toolkit for authorized testing of networks and devices.

**Developer:** Arman YB  
**Project:** WiFiSentinel  
**GitHub:** https://github.com/Armanyb1/wifisentinel

---

## Authorized Use Only

Use WiFiSentinel only on networks and devices that you own or have explicit permission to assess.

Do not use this project for unauthorized access, disruption, interception, credential theft, or attacks against third-party networks.

---

## Installation — Termux

### 1. Update Termux

Run:

    pkg update -y && pkg upgrade -y

### 2. Install required packages

    pkg install git python openssl curl wget -y

### 3. Install Python dependencies

    pip install -r requirements.txt

### 4. Run WiFiSentinel

    python app/main.py

---

## Configuration

Create your local environment file:

    cp .env.example .env

Never commit .env or real Telegram bot credentials to GitHub.

---

## License System

WiFiSentinel currently uses a local SQLite database for license records.

Each license is associated with a device ID and may contain a plan and expiration date.

---

## Telegram Bot

The Telegram component is intended for administrator-side license management.

Bot credentials are loaded from .env.

---

## Development Status

WiFiSentinel is currently under active development.

Current foundation:

- Device ID generation
- Local SQLite license storage
- License lookup
- License activation and revocation functions
- Basic Telegram configuration
- Termux support
