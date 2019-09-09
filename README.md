# Backup FreeOTP

A simple python script to backup [OTP tokens](https://en.wikipedia.org/wiki/One-time_password)
from the [FreeOTP Android app](https://play.google.com/store/apps/details?id=org.fedorahosted.freeotp).

To create backups you must use [adb](https://developer.android.com/studio/command-line/adb). This script just extracts the tokens from the backup archive and gereates qr codes to provide a simple restore process.

If [pyqrcode](https://github.com/mnooner256/pyqrcode) to be is installed, this script generates qr codes that can be scanned with FreeOTP.
Otherwise the [topt url](https://github.com/google/google-authenticator/wiki/Key-Uri-Format) is printed and
you can generate the qr code with a different tool.

Have fun!

## Installation

```bash
# Clone this repo
git clone git@github.com:raphiz/freeotp-backup.git
cd freeotp-backup/

# Optional: Create a virtual env and install optional dependencies
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Example Usage

```bash
# Create a backup of the App using ADB - don't encrypt it...
adb backup -f freeotp-backup.ab -apk org.fedorahosted.freeotp

python backup_freetop_codes.py freeotp-backup.ab
```

## Credits

- [The FreeOTP Android App](https://freeotp.github.io/)
- ["Backing up and recovering 2FA tokens from FreeOTP" by Marvin Contessi](https://gist.github.com/kontez/05923f2fc208c6bbe3de81f28de571db)
- [pyqrcode by Michael Nooner](https://github.com/mnooner256/pyqrcode)
- [StackOverflow Answer by Alex Martelli](https://stackoverflow.com/questions/29055634/python-unpack-android-backup#answer-29055723)
