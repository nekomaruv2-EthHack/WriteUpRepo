import subprocess
import os
import xml.etree.ElementTree as ET
import argparse
import re

work_dir = "/tmp/execute_enum"
os.makedirs(work_dir, exist_ok=True)
os.makedirs(os.path.join(work_dir, "nmap"), exist_ok=True)
os.chdir(work_dir)

def detect_redirect_host(target, protocol="http"):
    try:
        result = subprocess.run(
            ["curl", "-I", "-s", f"{protocol}://{target}"],
            capture_output=True, text=True, timeout=5
        )
        for line in result.stdout.splitlines():
            if line.lower().startswith("location:"):
                # URLからホスト名部分のみを抽出
                m = re.search(r"https?://([^/\s:]+)", line, re.IGNORECASE)
                if m:
                    return m.group(1)
    except Exception as e:
        print(f"[!] Error detecting redirect: {e}")
    return None

def add_hosts_entry(ip: str, hostname: str):
    """/etc/hosts にエントリを追加する"""
    if not hostname or hostname == ip:
        return
    print(f"[*] Adding {ip} {hostname} to /etc/hosts")
    entry = f"{ip} {hostname}"
    try:
        subprocess.run(
            f"grep -qxF '{entry}' /etc/hosts || echo '{entry}' | sudo tee -a /etc/hosts",
            shell=True, check=True, capture_output=True
        )
    except subprocess.CalledProcessError:
        print("[!] Failed to add hosts entry. Root privileges may be required.")

def run_ffuf(target_host, mode="directory"):
    """ffufを実行する (directory / subdomain)"""
    wordlist_dir = "/usr/share/wordlists/seclists/Discovery/Web-Content/common.txt"
    wordlist_sub = "/usr/share/wordlists/seclists/Discovery/DNS/subdomains-top1million-5000.txt"
    
    if mode == "directory":
        print(f"[*] Fuzzing directories on {target_host}...")
        cmd = f"ffuf -u http://{target_host}/FUZZ -w {wordlist_dir} -mc 200 -s"
    else:
        print(f"[*] Fuzzing subdomains on {target_host}...")
        cmd = f"ffuf -u http://{target_host} -H 'Host: FUZZ.{target_host}' -w {wordlist_sub} -mc 200 -s"
    
    subprocess.run(cmd, shell=True)

def nmap_scan(target):
    """Nmapを実行し、80/443が空いていればWebの精査に移行する"""
    print(f"[*] Executing nmap to {target}...")
    nmap_cmd = f"sudo nmap -sT -sC -sV -vv -oA nmap/nmap_result -oX nmap.xml {target}"
    subprocess.run(nmap_cmd, shell=True)

    if not os.path.exists("nmap.xml"):
        print("[!] Nmap XML output not found.")
        return

    tree = ET.parse("nmap.xml")
    root = tree.getroot()

    is_web_open = False
    found_host = target

    for port in root.iter("port"):
        portid = port.get("portid")
        state_el = port.find("state")
        if state_el is None or state_el.get("state") != "open":
            continue

        if portid in ["80", "443"]:
            is_web_open = True
            proto = "https" if portid == "443" else "http"
            redirected = detect_redirect_host(target, proto)
            if redirected:
                found_host = redirected
                add_hosts_entry(target, found_host)

    if is_web_open:
        run_ffuf(found_host, mode="directory")
        run_ffuf(found_host, mode="subdomain")

def main():
    parser = argparse.ArgumentParser(description="Auto Enumeration Tool")
    parser.get_default("target")
    parser.add_argument("target", help="target IP")
    args = parser.parse_args()

    nmap_scan(args.target)

if __name__ == "__main__":
    main()