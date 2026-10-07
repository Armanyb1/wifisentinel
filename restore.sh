#!/data/data/com.termux/files/usr/bin/bash
set -e

echo "WiFiSentinel Restore"

pkg update -y
pkg install -y python git

cd ~

if [ ! -d "$HOME/wifisentinel" ]; then
    git clone git@github.com:Armanyb1/wifisentinel.git
fi

cd "$HOME/wifisentinel"

python -m pip install -r requirements.txt

if [ -f "$HOME/storage/shared/wifisentinel-private-backup.tar.gz" ]; then
    tar -xzf "$HOME/storage/shared/wifisentinel-private-backup.tar.gz" -C "$HOME/wifisentinel"
    echo "Private backup restored."
else
    echo "Private backup not found."
fi

echo "WiFiSentinel restore complete."
