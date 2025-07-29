# ftp-scan
A powerful and modular Python-based FTP vulnerability scanner for Linux systems, built for penetration testers, VAPT analysts, and cybersecurity learners. This tool identifies anonymous login, FTP banner/version, vulnerabilities, and supports full port range scanning with CLI options.

# 🔍 FTP VAPT Scanner (2025 Edition)

A Linux-compatible FTP vulnerability scanner for penetration testers and cybersecurity analysts.

---

## 🚀 Features
- 🔍 Port 21 FTP scan
- 🌐 Full port scan with `-p-`
- 🔐 Anonymous login detection
- 📄 File listing from anonymous login
- 🎯 Target CIDR/network scan
- 🧠 Verbose logging with `-v`
- 💾 Save credentials with `-o`
- 📡 Banner grabbing & vulnerability match
- 🆘 Help menu with `-h` / `--help`

---

## 📥 How to Install

> 🔧 **Prerequisites:**  
> - Python 3.x  
> - Linux system (Kali, Parrot OS, Ubuntu, etc.)

### 🧪 Step-by-step:

```bash
# 1. Clone the repository
git clone https://github.com/yourname/ftp-vapt-scan.git
cd ftp-vapt-scanner

# 2. (Optional) Create a virtual environment
python3 -m venv venv
source venv/bin/activate

# 3. Run the scanner
python3 ftp-scan.py -h


## 📦 Usage

python3 ftp-scan.py -t 192.168.1.10
python3 ftp-scan.py -t 192.168.1.0/24 -p- -v -o result.txt

``` 
---

## ✍ Author

*Coded by:* [404Nexus](https://github.com/404Nexus)  
🔍 Bug Bounty Hunter | 🛡 Ethical Hacker | ⚙ VAPT | 📅 2025

---
