# PowerView Comprehensive Enumeration Cheat Sheet

> **DISCLAIMER & LEGAL NOTICE**
> This reference guide is strictly for educational purposes, security research, and authorized penetration testing within controlled lab environments or authorized engagements. Unauthorized scanning, enumeration, or exploitation of networks without explicit written consent is illegal. Always perform these activities strictly within an authorized scope.

---

## 1. PowerView Syntax & Parameter Reference

PowerView functions support standardized PowerShell parameters for filtering, searching, and formatting LDAP queries efficiently.

### Core Parameters

| Parameter | Description & Example Syntax |
| :--- | :--- |
| `-Identity` | Target a specific object by `sAMAccountName`, `DN`, `GUID`, or `SID`.<br>`Get-DomainUser -Identity "jdoe"` |
| `-Properties` | Specify specific LDAP attributes to return (speeds up query execution).<br>`Get-DomainUser -Properties samaccountname, description` |
| `-LDAPFilter` | Raw LDAP filter executed directly on the Domain Controller (fastest).<br>`Get-DomainUser -LDAPFilter "(samaccounttype=805306368)"` |
| `-CustomFilter` | PowerShell-style filter expression evaluated prior to returning objects.<br>`Get-DomainUser -CustomFilter "(pwdlastset -eq 0)"` |
| `-SearchBase` | Restrict search scope to a specific OU or container Distinguished Name.<br>`Get-DomainUser -SearchBase "OU=Employees,DC=domain,DC=local"` |
| `-SearchScope` | Limit LDAP search depth (`Base`, `OneLevel`, or `Subtree`).<br>`Get-DomainObject -SearchScope OneLevel` |
| `-Server` | Target a specific Domain Controller or Global Catalog server.<br>`Get-DomainUser -Server "DC01.domain.local"` |
| `-Recurse` | Recursively expand nested group memberships or dependencies.<br>`Get-DomainGroupMember -Identity "Domain Admins" -Recurse` |
| `-ResolveGUIDs` | Translate binary GUIDs in ACL entries to human-readable names.<br>`Get-DomainObjectAcl -Identity "Domain Admins" -ResolveGUIDs` |

---

## 2. Domain, Forest & Trust Enumeration

| Command | Description |
| :--- | :--- |
| `Get-Domain` | Retrieve core domain information (Name, SID, Domain Controllers). |
| `Get-DomainSID` | Returns the Security Identifier (SID) for the current domain. |
| `Get-DomainController` | List all Domain Controllers in the current domain. |
| `Get-DomainPolicyData` | Retrieve password complexity, lockout policies, and Kerberos settings. |
| `Get-DomainForest` | Query forest configuration, domain trees, and Global Catalog servers. |
| `Get-DomainForestDomain` | List all domains residing within the forest. |
| `Get-DomainTrust` | List domain trust relationships for the current domain. |
| `Get-DomainForestTrust` | List inter-forest trust relationships. |

---

## 3. User Account & UAC Enumeration

### User Enumeration Commands

| Command | Description |
| :--- | :--- |
| `Get-DomainUser` | List all domain user objects. |
| `Get-DomainUser -Identity <user>` | View all attributes for a specific user. |
| `Get-DomainUser -SPN` | Find accounts with Service Principal Names (**Kerberoasting**). |
| `Get-DomainUser -PreauthNotRequired` | Find accounts with Pre-Authentication disabled (**AS-REP Roasting**). |
| `Get-DomainUser -AdminCount` | Find protected user accounts (`adminCount=1`). |
| `Get-DomainUser -AllowDelegation` | Find accounts not marked as sensitive (can be delegated). |

### Key User Account Control (UAC) Flags

The `userAccountControl` (UAC) attribute defines account states. Below are key security-relevant UAC flags:

| UAC Flag | Hex / Value | Security Significance | PowerView Equivalent / Filter |
| :--- | :--- | :--- | :--- |
| `ACCOUNTDISABLE` | `0x0002` | Account is currently disabled. | Filter out with `(userAccountControl:1.2.840.113556.1.4.803:=2)` |
| `PASSWD_NOTREQD` | `0x0020` | Password is not required. | `Get-DomainUser -CustomFilter "(useraccountcontrol -band 32)"` |
| `DONT_EXPIRE_PASSWORD` | `0x10000` | Password never expires. | `Get-DomainUser -CustomFilter "(useraccountcontrol -band 65536)"` |
| `DONT_REQ_PREAUTH` | `0x400000` | Kerberos Pre-Auth Disabled. | `Get-DomainUser -PreauthNotRequired` |
| `TRUSTED_FOR_DELEGATION` | `0x80000` | Unconstrained Delegation. | `Get-DomainUser -Unconstrained` |
| `TRUSTED_TO_AUTH_FOR_DELEGATION` | `0x1000000` | Constrained Delegation. | `Get-DomainUser -TrustedToAuth` |

---

## 4. Group & Membership Enumeration

| Command | Description |
| :--- | :--- |
| `Get-DomainGroup` | List all groups in the domain. |
| `Get-DomainGroup -Identity "<group>"` | View detailed properties for a specific group. |
| `Get-DomainGroupMember -Identity "<group>"` | List members of a specific group. |
| `Get-DomainGroupMember -Identity "Domain Admins" -Recurse` | Recursively list direct and nested members of Domain Admins. |
| `Get-DomainGroup -MemberIdentity <user>` | List all groups a specific user belongs to. |
| `Get-DomainForeignGroupMember` | Find members of local groups that originate from trusted foreign domains. |
| `Get-DomainForeignUser` | List foreign users explicitly granted access or memberships. |

---

## 5. Computers, Shares, Sessions & LAPS

| Command | Description |
| :--- | :--- |
| `Get-DomainComputer` | List all computer objects in the domain. |
| `Get-DomainComputer -OperatingSystem "*Server*"` | Filter domain computers by operating system. |
| `Get-DomainComputer -Unconstrained` | Find computers with Unconstrained Kerberos Delegation. |
| `Find-DomainShare` | Enumerate accessible SMB network shares across domain machines. |
| `Find-DomainShare -CheckShareAccess` | Verify read/write access permissions on discovered shares. |
| `Get-NetSession -ComputerName <target>` | List active network sessions on a remote host. |
| `Get-DomainUserEvent` | Query event logs on DCs to identify active user logon sessions. |
| `Get-LAPSProperty` | Read LAPS passwords (if account has necessary permissions). |

---

## 6. Organizational Units (OUs) & Group Policy (GPOs)

| Command | Description |
| :--- | :--- |
| `Get-DomainOU` | List all Organizational Units in the domain. |
| `Get-DomainOU -Identity "<OU_Name>"` | Retrieve details for a specific Organizational Unit. |
| `(Get-DomainUser -SearchBase "OU=<OU>,DC=<domain>").Count` | Count total users within a specific OU. |
| `Get-DomainGPO` | List all Group Policy Objects (GPOs). |
| `Get-DomainGPOLocalGroup` | Query GPO settings that modify local group memberships. |
| `Get-DomainGPOComputerLocalGroup` | Map local administrator group memberships managed via GPO. |

---

## 7. Kerberos Delegation Enumeration

| Delegation Type | PowerView Enumeration Command | Attack / Security Context |
| :--- | :--- | :--- |
| **Unconstrained** | `Get-DomainUser -Unconstrained`<br>`Get-DomainComputer -Unconstrained` | Account stores TGTs of users authenticating to it. |
| **Constrained (Protocol Transition)** | `Get-DomainUser -TrustedToAuth`<br>`Get-DomainComputer -TrustedToAuth` | Service can impersonate any user to specified target SPNs via S4U2Self/S4U2Proxy. |
| **Constrained (AllowedToDelegate)** | `Get-DomainUser -CustomFilter "(msDS-AllowedToDelegateTo=*)"` | Lists target SPNs an account is authorized to delegate to. |
| **Resource-Based (RBCD)** | `Get-DomainComputer -CustomFilter "(msDS-AllowedToActOnBehalfOfOtherIdentity=*)"` | Machine allows specified security principals to configure delegation against it. |

---

## 8. Active Directory ACLs & Rights Enumeration

### Critical Abusable Access Rights

* `GenericAll`: Full control over the target object.
* `GenericWrite` / `WriteProperty`: Ability to modify object attributes (e.g., reset passwords, add SPNs, set RBCD).
* `WriteDacl`: Ability to modify security permissions on the target object.
* `WriteOwner`: Ability to take ownership of the target object.
* `AllExtendedRights` / `ForceChangePassword`: Force password reset without knowing current password.

### ACL Enumeration Commands

| Command | Description |
| :--- | :--- |
| `Get-DomainObjectAcl -Identity <object>` | Retrieve DACL for a specific object. |
| `Get-DomainObjectAcl -Identity "Domain Admins" -ResolveGUIDs` | Retrieve DACL with human-readable rights and GUIDs. |
| `Add-DomainObjectAclTarget -TargetIdentity <user>` | Find objects where a specific account has explicit rights. |
| `Find-InterestingDomainAcl -ResolveGUIDs` | Scan the domain for non-default or abusable ACL permissions. |

---

## 9. Balanced Scenario Playbooks

### Playbook 1: Domain Reconnaissance & Policy Audit
```powershell
# Get basic domain info, SID, and password policy
Get-Domain
Get-DomainSID
Get-DomainPolicyData
```

### Playbook 2: Kerberos Hash Hunting (Kerberoasting & AS-REP Roasting)
```powershell
# Export Kerberoastable user accounts
Get-DomainUser -SPN | Where-Object {$_.samaccountname -notlike "*$"} | Select-Object samaccountname, servicePrincipalName

# Export AS-REP Roastable accounts
Get-DomainUser -PreauthNotRequired | Select-Object samaccountname, useraccountcontrol
```

### Playbook 3: Privileged Groups & High-Value Account Discovery
```powershell
# Recursively enumerate Domain Admins
Get-DomainGroupMember -Identity "Domain Admins" -Recurse | Select-Object MemberName, MemberDistinguishedName

# Find accounts with adminCount = 1
Get-DomainUser -AdminCount | Select-Object samaccountname, memberof
```

### Playbook 4: Delegation & Misconfiguration Hunting
```powershell
# Find Unconstrained Delegation servers (excluding Domain Controllers)
Get-DomainComputer -Unconstrained | Where-Object {$_.primarygroupid -ne 516} | Select-Object name

# Find Constrained Delegation accounts
Get-DomainUser -CustomFilter "(msDS-AllowedToDelegateTo=*)" | Select-Object samaccountname, msDS-AllowedToDelegateTo
```

### Playbook 5: Network Share & GPO Reconnaissance
```powershell
# Find accessible SMB shares across the domain
Find-DomainShare -CheckShareAccess

# Find local admin groups managed via GPO
Get-DomainGPOComputerLocalGroup
```

---

## 10. Quick Command Summary Table

| Category | Primary PowerView Command |
| :--- | :--- |
| **Domain** | `Get-Domain`, `Get-DomainPolicyData`, `Get-DomainTrust` |
| **Users** | `Get-DomainUser`, `Get-DomainUser -SPN`, `Get-DomainUser -PreauthNotRequired` |
| **Groups** | `Get-DomainGroup`, `Get-DomainGroupMember -Identity "Domain Admins" -Recurse` |
| **Computers** | `Get-DomainComputer`, `Get-DomainComputer -Unconstrained` |
| **Shares** | `Find-DomainShare -CheckShareAccess` |
| **OUs / GPOs** | `Get-DomainOU`, `Get-DomainGPO`, `Get-DomainGPOComputerLocalGroup` |
| **ACLs** | `Find-InterestingDomainAcl -ResolveGUIDs`, `Get-DomainObjectAcl` |