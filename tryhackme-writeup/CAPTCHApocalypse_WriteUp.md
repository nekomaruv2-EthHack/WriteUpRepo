# CAPTCHApocalypse
- TargetIP: 10.144.137.139
## recon
1. port scan

`nmap -sT -sV -Pn -n 10.144.137.139`

```
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.9 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
```

2. sub directory can

`ffuf -u http://10.144.137.139/FUZZ -w /usr/share/wordlists/SecLists/Discovery/Web-Content/common.txt -mc 200.302`
```
index.php
```
No specific hidden page maybe.

`curl -iL http://10.144.137.139`

No Redirect. So I feel hardly to find sub domain of it.


In this time, route to capture the flag is visiting to port 80 and maybe ssh to 22. 
If I may be so bold, I want privlige escalation to root.
(In hindsight, there was no need to gain access to the shell; all we had to do was bypass the authentication.)

