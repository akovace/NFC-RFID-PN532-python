# NFC-RFID-PN532-python
Hardver:
- Raspberry pi 3
- PN532 NFC modul
- ribbon kabel

Softver:
- Driveri: https://www.itead.cc/blog/raspberry-pi-drives-itead-pn532-nfc-module-with-libnfc
uz izmjenu device.connstring = "pn532_spi:/dev/spidev0.0:500000" u
device.connstring = "pn532_spi:/dev/spidev0.0"

- recent.py
aplikacija napisana u pythonu koja "sluša" gore navedene drivere. Naredba za slušanje čitača u terminalu je nfc-mfsetuid i nfc-poll. Koristili smo nfc-mfsetuid. Unutar recent.py ubacili smo nfc-mfsetuid i prislonom nfc taga dobijemo njezinje podatke. Daljnjom obradom podataka izvučen je UID taga. Nakon što skripza podupi podatak, čuje se zvuk.



