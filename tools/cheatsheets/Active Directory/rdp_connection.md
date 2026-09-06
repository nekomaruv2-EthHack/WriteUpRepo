## xfreerdp3

#### Example: 
```
xfreerdp3 \
  /v:10.129.204.177 \
  /u:robert \
  /p:'Inlanefreight01!' \
  /drive:loot,$HOME/Desktop/loot \
  /clipboard \
  /dynamic-resolution \
  /cert:ignore
```

#### check
```
Test-Path '\\tsclient\loot\'
```
- expect "true" if not, try.  logofto kill the session and re-try

#### Move files from shared folder
```
Copy-Item C:\Tools\*.zip \\tsclient\loot\
```
