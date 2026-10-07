#!/data/data/com.termux/files/usr/bin/bash
set -e
pkg install python openssl curl wget -y
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
echo "WiFiSentinel installation complete."
