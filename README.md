# NFC-RFID-PN532-python
[HR]
Koljegij: Projektiranje informatičkih projekata, 
Sveučilište Jurja Dobrile u Puli, OIKT, 
Projekt: Sustav za evidenciju - "Recent"

[EN]
Course: Designing IT systems
Juraj Dobrila University of Pula, OIKT
Project: Employee records system - "Recent"

Hardver (hardware):
- Raspberry pi 3
- PN532 NFC modul
- ribbon kabel (cable)

Softver: [HR]
- Driveri: https://www.itead.cc/blog/raspberry-pi-drives-itead-pn532-nfc-module-with-libnfc
uz izmjenu device.connstring = "pn532_spi:/dev/spidev0.0:500000" u 'device.connstring' = "pn532_spi:/dev/spidev0.0"

Software: [EN]
- Drivers: https://www.itead.cc/blog/raspberry-pi-drives-itead-pn532-nfc-module-with-libnfc
you need to change: 'device.connstring' = "pn532_spi:/dev/spidev0.0:500000" into 'device.connstring' = "pn532_spi:/dev/spidev0.0"

- recent.py [HR]
aplikacija napisana u pythonu koja "sluša" gore navedene drivere. Naredba za slušanje čitača u terminalu je nfc-mfsetuid i nfc-poll. Koristili smo nfc-mfsetuid. Unutar recent.py ubacili smo nfc-mfsetuid i prislonom nfc taga dobijemo njezinje podatke. Daljnjom obradom podataka izvučen je UID taga. Nakon što skripta podupi podatak, čuje se zvuk.

- recent.py [EN]
Recent.py is written for "listening" libnfc functions. Terminal commands for NFC reader/writer data are 'nfc-mfsetuid' and 'nfc-poll'. In this file I'm using 'nfc-mfsetuid' for nfc tag's data. For every card/tag python file displays UID data, and plays a sound indicating card/tag is read. 


============================
============================
#RecENT basic info
RecENT is application which is developed for companies and organizations that want to upgrade their way of managing employees work hours. 
RecENT contains from:
  *  Web application;
  *  Mobile application;
  *  Record device - Raspberry Pi with NFC reader;

### Web application 
Through web application, company administration and accounting can get periodic(e.g. monthly) reports and manage employees work hours. 
GitHub: https://github.com/m-petkovic/projekt

### Mobile application
Mobile app is used by employees to record their arrival and departure form work. To record their arrival or departure, employee places his smartphone on record device, and trough installed RecENT mobile app and NFC sensor, he/she makes his checkout. 
GitHub: https://github.com/m-petkovic/recentAndroid

### Record device
Record device is placed on entrace of building or area where your employees work, so they can easly make a checkout. Record device is made of Raspberry Pi and NFC reader, and it requires a constant network connection for running.
GitHub: https://github.com/akovace/NFC-RFID-PN532-python

** For more info visit ** [RecENT webapge](http://recent.cekomat.com)

======================= 
