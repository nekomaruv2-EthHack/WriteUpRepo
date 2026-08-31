# Windows `net` Command Cheatsheet for Penetration Testing & Active Directory

A comprehensive cheatsheet for enumeration, user management, and administration using the Windows `net` command in internal network assessments and Active Directory environments.

## 1. User Management (ユーザー管理)

### List all local users
```powershell
net user
```

### View details of a specific local user
```powershell
net user <username>
```

### View details of a domain user
```powershell
net user <username> /domain
```

### Create a new local user
```powershell
net user <username> <password> /add
```

### Create a new domain user (run on DC or with appropriate privileges)
```powershell
net user <username> <password> /add /domain
```

### Delete a local user
```powershell
net user <username> /delete
```

### Change a user's password
```powershell
net user <username> <new_password>
```

### Enable or disable a user account
```powershell
net user <username> /active:yes
net user <username> /active:no
```

---

## 2. Group Management (グループ管理)

### List all local groups
```powershell
net localgroup
```

### View members of the local Administrators group
```powershell
net localgroup administrators
```

### Add a user to a local group
```powershell
net localgroup administrators <username> /add
```

### Remove a user from a local group
```powershell
net localgroup administrators <username> /delete
```

### List global domain groups
```powershell
net group /domain
```

### View members of the Domain Admins group
```powershell
net group "Domain Admins" /domain
```

### View members of a specific domain group
```powershell
net group "<Group Name>" /domain
```

### Add a user to a domain group
```powershell
net group "<Group Name>" <username> /add /domain
```

---

## 3. Domain & Account Information (ドメイン・アカウント情報)

### View domain information and available domains
```powershell
net view /domain
```

### View computers joined to a specific domain
```powershell
net view /domain:<DomainName>
```

### View shared resources on a specific computer
```powershell
net view \\<ComputerName>
```

### View local password and lockout policies
```powershell
net accounts
```

### View domain-wide account and password policies
```powershell
net accounts /domain
```

---

## 4. Shares & Sessions (共有・セッション管理)

### List shared resources on the local machine
```powershell
net share
```

### Create a new local share
```powershell
net share <ShareName>=<FolderPath> /grant:<Username>,FULL
```

### Delete a local share
```powershell
net share <ShareName> /delete
```

### Map a network share (Drive mapping)
```powershell
net use Z: \\<Target-IP>\<ShareName> <Password> /user:<Username>
```

### Disconnect a network share
```powershell
net use Z: /delete
```

### View active sessions connected to the machine
```powershell
net session
```

### View active connections from your machine to others
```powershell
net use
```

---

## 5. Service & Network Configuration (サービス・ネットワーク確認)

### List running services
```powershell
net start
```

### Start a specific service
```powershell
net start <ServiceName>
```

### Stop a specific service
```powershell
net stop <ServiceName>
```

### Check network statistics
```powershell
net statistics workstation
net statistics server
```