# ftp-scan
A powerful and modular Python-based FTP vulnerability scanner for Linux systems, built for penetration testers, VAPT analysts, and cybersecurity learners. This tool identifies anonymous login, FTP banner/version, vulnerabilities, and supports full port range scanning with CLI options.

# 🔍 FTP VAPT Scanner (2025 Edition)

A Linux-compatible FTP vulnerability scanner for penetration testers and cybersecurity analysts.

## 🚀 Features
- Full port scan with `-p-`
- Anonymous login detection
- Banner grabbing & vulnerable version match
- Save anonymous creds with `-o`
- Verbose mode with `-v`
- Target single IP or subnet
- Help menu with `-h` or `--help`

## 📦 Usage

```bash
python3 ftp-scan.py -t 192.168.1.10
python3 ftp-scan.py -t 192.168.1.0/24 -p- -v -o result.txt

