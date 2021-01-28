![GitHub repo size](https://img.shields.io/github/repo-size/yuvrajraghuvanshis/WhatsApp-Key-Database-Extractor?color=informational&label=repo%20size)
![GitHub top language](https://img.shields.io/github/languages/top/yuvrajraghuvanshis/WhatsApp-Key-Database-Extractor)
![License](https://img.shields.io/github/license/yuvrajraghuvanshis/WhatsApp-Key-Database-Extractor?label=license)
![Depends](https://img.shields.io/badge/depends-JAVA-informational)
![visitors](https://visitor-badge.glitch.me/badge?page_id=yuvrajraghuvanshis.whatsapp-key-database-extractor)


<br />

![Windows](https://img.shields.io/badge/windows-tested-success)
![Kali](https://img.shields.io/badge/kali-tested-success)
![Ubuntu](https://img.shields.io/badge/ubuntu-tested-success)
![OSX](https://img.shields.io/badge/mac-not%20tested-orange)


<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/yuvrajraghuvanshis/WhatsApp-Key-Database-Extractor">
    <img src="https://raw.githubusercontent.com/yuvrajraghuvanshis/WhatsApp-Key-Database-Extractor/master/helpers/banner.png" alt="Logo" width="320" height="100">
  </a>

  <h3 align="center">WhatsApp Key/DataBase Extractor</h3>

  <p align="center">
    Extract key/msgstore.db from /data/data/com.whatsapp in android without root.
    <br />
</p>


![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/aqua.png)

<details><summary>Table of Contents</summary>

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
  * [Standalone Operations](#standalone-operations)
  * [Troubleshooting](#troubleshooting)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [License](#license)
* [Agreement](#agreement)
* [Contact](#contact)
</details>

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/aqua.png)

## About The Project

<!--[![Glimpse][product-screenshot]](https://github.com/yuvrajraghuvanshis/WhatsApp-Key-Database-Extractor)-->

This project is inspired by [EliteAndroidApps/WhatsApp-Key-DB-Extractor](https://github.com/EliteAndroidApps/WhatsApp-Key-DB-Extractor). Since Android v4.0+ Google has removed adb backup  and apps no longer supported being abcked up by "adb backup -f myApp.ab -apk com.foobar.app". However there is one catch in this scenario and that is some old version of many apps including WhatsApp support that to this day, and that's the idea...

The idea is to install "Legacy Version" of WhatsApp on you device via adb and use "adb backup"  to fetch files from "/data/data/com.whatsapp" folder which includes both the 'key' and 'msgstore.db' (non encrypted) file and after that restore current WhatsApp.

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/aqua.png)

### Built With
* [Python](https://www.python.org/)
* [Bash](https://www.gnu.org/software/bash/) (for Linux and OS X)
#### Depends upon    
* [Java](https://www.java.com/) (To extract backup)

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/aqua.png)

## Getting Started

Before doing anything take a backup of your chats and turn off your phone's internet so you don't lose any new messages.
For that go to 'WhatsApp settings\Chat Settings\Chat Backup' here take a local bacakup. Prepare for Worst.               
After [intallation](#installation) follow on screen instructions.

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/aqua.png)

### Prerequisites

* O/S: Any windows/Mac/Linux. Do not have access to any of these? Try [Termux Edition.](https://github.com/yuvrajraghuvanshis/WhatsApp-Key-Database-Extractor/tree/termux) 
* [Python 3.x](https://www.python.org/downloads/)
* [Java](https://www.java.com/en/download/)
* [ADB Drivers](https://developer.android.com/studio/releases/platform-tools) 
* USB Debugging must be enabled on the target device. Settings -> Developer Options -> (Debugging) USB debugging  
     If you cannot find Developer Options then please go to: Settings -> About phone/device and tap the Build number multiple times until you're finally declared a developer.  
* Android device with Android 4.0 or higher. i.e. Ice Cream Sandwich, Jelly Bean, KitKat, Lollipop, Marshmallow, Nougat, Oreo, Pie, Q.  


![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/aqua.png)

### Installation

1. Clone the repo
```bash
git clone https://github.com/yuvrajraghuvanshis/WhatsApp-Key-Database-Extractor.git && cd WhatsApp-Key-Database-Extractor
```
2. Get python requirements
```python
python3 -m pip install -r requirements.txt
```
3. Install Dependencies (for linux and OSX)
```bash
chmod +x bin/linux_dependencies.sh
sudo ./bin/linuxdependencies.sh
```
4. Run `wa_kdbe.py`
```python
python3 wa_kdbe.py
```
4.1 Enter `device serial id`
```
List of devices attached 
0123a4b5678	device
Choose device from "List of devices attached" : __________
(Copy paste your device serial id from above, i.e. 0123a4b5678)
```

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/aqua.png)

### Standalone operations
<details><summary>Click to expand</summary>These operations are standalone implementation of their defined task. One need to run these when specifically needed. For ex : Process finished but WhatsApp was not reinstalled on device.

1. Run `view_extract.py` : To 'Fluff' whatsapp.ab to whatsapp.tar and extract files.
```
python view_extract.py

IMP : For this to work there should be 'whatsapp.ab' file either in 'extracted/<userName>' folder or in 'tmp' folder.
```

2. Run `protect.py` : To compress/decompress user folder with(out) password for safekeeping.
```
python protect.py

IMP : For this to work there should either be "userName" folder or "userName.7z" file in 'extracted' folder. Where "userName" is reference user name you entered earlier.
```

3. Run `restore.py` : To reinstall WhatsApp on device.
```
python restore.py
```
</details>

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/aqua.png)

### Troubleshooting

```bash
List of devices attached 
0123a4b5678	device
emulator-5554 unauthorized
```
* Choose device from "List of devices attached" : 0123a4b5678
* If list is empty close terminal, remove and replug the device, and re-run the script. [Read More](https://github.com/YuvrajRaghuvanshiS/WhatsApp-Key-Database-Extractor/issues/11#issuecomment-768500899)
* If you have never used USB Debugging before, you may also need to verify the fingerprint.  
* If you have set a default backup password in your Android settings, then this MUST be the  backup password that you PROVIDE when prompted to backup your data. Else it WILL fail!  
* If you get an error saying "AES encryption not allowed" then you need to update your Oracle Java Cryptography Extension (JCE) to Unlimited Strength Jurisdiction Policy Files.  
* WhatsApp crashing? Run `python3 restore_whatsapp.py`. Or "clear data/storage" / uninstall and reinstall from Play Store.


![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/aqua.png)

## Roadmap

See the [open issues](https://github.com/yuvrajraghuvanshis/WhatsApp-Key-Database-Extractor/issues) for a list of proposed features (and known issues).
#### ToDo
* ![Status](https://img.shields.io/badge/Status-Done-success) Zip extracted folder with password.
* ![Status](https://img.shields.io/badge/Status-Removed-red) Command line arguments

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/aqua.png)

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/aqua.png)

## License

Distributed under the MIT License. See `LICENSE` for more information.

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/aqua.png)

## Agreement

I made this project because it was hard for me to kill time and the other one was very old. 
This tool is provided "as-is" and hence you will be responsible however you use it. Cheers☕

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/aqua.png)

## Contact

Yuvraj Raghuvanshi - [Send me a mail](mailto:YuvrajRaghuvanshi.S%40protonmail.com?subject=From%20GitHub%20WA-KDBE%20:%20%3CAdd%20subject%20here.%3E "Send me a mail, Don't change subject line.")

Project Link: [https://github.com/yuvrajraghuvanshis/WhatsApp-Key-Database-Extractor](https://github.com/yuvrajraghuvanshis/WhatsApp-Key-Database-Extractor)

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/aqua.png)

[license-url]: https://github.com/yuvrajraghuvanshis/WhatsApp-Key-Database-Extractor/blob/master/LICENSE
[product-screenshot]: https://raw.githubusercontent.com/yuvrajraghuvanshis/WhatsApp-Key-Database-Extractor/master/helpers/banner.png
