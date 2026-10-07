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

```
pkg update -y && pkg upgrade -y


pkg install git python openssl curl wget -y

pip install -r requirements.txt

python app/main.py
```


---

## Configuration

Create your local environment file:

`cp .env.example .env`

Never commit `.env` or real Telegram bot credentials to GitHub.

---

## লাইসেন্স ও অ্যাক্টিভেশন

WiFiSentinel একটি **Device ID-ভিত্তিক License System** ব্যবহার করে।

### কীভাবে লাইসেন্স নেবেন

1. WiFiSentinel Install করুন।
2. Application চালিয়ে আপনার **Device ID** দেখুন।
3. Telegram Bot-এ যান: **@Hack_Yb_bot**
4. `/pricing` লিখে বর্তমান License Plan ও মূল্য দেখুন।
5. Purchase করার পর আপনার **Device ID** Administrator-কে পাঠান।
6. Administrator আপনার Device ID-এর জন্য License Activate করবেন।

### License Plan ও মূল্য

বর্তমান Plan ও মূল্য Telegram Bot-এর `/pricing` command-এর মাধ্যমে দেখা যাবে।

⚠️ আপনার `.env` ফাইল বা Telegram Bot Token কারও সাথে শেয়ার করবেন না।

---

## Telegram Bot

### Customer Commands

`/start` — Bot শুরু করুন  
`/help` — Available commands দেখুন  
`/status` — Bot online আছে কিনা দেখুন  
`/pricing` — License Plan ও মূল্য দেখুন

### Administrator

License activation এবং revocation শুধুমাত্র Administrator-এর জন্য অনুমোদিত।

---

## Development Status

WiFiSentinel বর্তমানে active development-এর মধ্যে রয়েছে।

### Current Foundation

- Device ID generation
- Local SQLite license storage
- License lookup
- License activation
- License revocation
- Telegram Bot configuration
- Telegram license management foundation
- Termux support

---

## Security Notice

Never publish or share:

- Telegram Bot Token
- `.env` file
- Private credentials
- Private keys

Use WiFiSentinel only for authorized security assessment and diagnostic purposes.
