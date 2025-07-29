#!/usr/bin/env python3

import argparse, socket, ftplib, ipaddress, threading
from datetime import datetime

VULN_LIST = "vulnerable_versions.txt"

def scan_target(host, ports, verbose=False, save_file=None):
    for port in ports:
        try:
            with socket.create_connection((host, port), timeout=3) as s:
                banner = s.recv(1024).decode().strip()
                if verbose:
                    print(f"[+] {host}:{port} - Banner: {banner}")
                else:
                    print(f"[+] {host}:{port} - OPEN")

                if is_vulnerable(banner):
                    print(f"[!] {host}:{port} - Vulnerable FTP Detected: {banner}")

                check_anon_login(host, port, save_file)

        except Exception:
            if verbose:
                print(f"[-] {host}:{port} - Connection failed")

def is_vulnerable(banner):
    try:
        with open(VULN_LIST, "r") as f:
            for line in f:
                if line.strip() in banner:
                    return True
    except:
        pass
    return False

def check_anon_login(host, port, save_file=None):
    try:
        ftp = ftplib.FTP()
        ftp.connect(host, port, timeout=5)
        ftp.login('anonymous', 'anonymous@domain.com')
        print(f"[+] Anonymous Login Allowed on {host}:{port} ✅")
        files = ftp.nlst()
        for f in files:
            print(f"    └─ {f}")
        if save_file:
            with open(save_file, 'a') as f:
                f.write(f"{host}:{port} - Anonymous Login ✅\n")
        ftp.quit()
    except ftplib.error_perm:
        print(f"[-] Anonymous login not allowed on {host}:{port}")
    except Exception:
        print(f"[-] Could not connect/login to {host}:{port}")

def parse_targets(target):
    targets = []
    try:
        if "/" in target:
            net = ipaddress.IPv4Network(target, strict=False)
            targets = [str(ip) for ip in net.hosts()]
        else:
            targets = [target]
    except:
        print("[-] Invalid target format")
    return targets

def main():
    parser = argparse.ArgumentParser(description="FTP VAPT Scanner - by Kuldeep (2025)")
    parser.add_argument("-t", "--target", required=True, help="Target IP or CIDR (e.g., 192.168.1.1 or 192.168.1.0/24)")
    parser.add_argument("-p-", "--allports", action="store_true", help="Scan all ports (1-65535)")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose mode")
    parser.add_argument("-o", "--output", help="Save anonymous login results to file")
    args = parser.parse_args()

    ports = range(1, 65536) if args.allports else [21]
    targets = parse_targets(args.target)

    start = datetime.now()
    print(f"[*] Scan started at {start.strftime('%H:%M:%S')}")

    for host in targets:
        thread = threading.Thread(target=scan_target, args=(host, ports, args.verbose, args.output))
        thread.start()

if __name__ == "__main__":
    main()
