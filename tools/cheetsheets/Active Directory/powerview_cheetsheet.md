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
| `-LDAPFilter` | Raw LDAP filter executed directly on the Domain Controller (fastest & standard).<br>`Get-DomainUser -LDAPFilter "(samaccounttype=805306368)"` |
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
| `Get-ForestTrust` | List inter-forest trust relationships. |

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
| `PASSWD_NOTREQD` | `0x0020` | Password is not required. | `Get-DomainUser -LDAPFilter '(userAccountControl:1.2.840.113556.1.4.803:=32)'` |
| `DONT_EXPIRE_PASSWORD` | `0x10000` | Password never expires. | `Get-DomainUser -LDAPFilter '(userAccountControl:1.2.840.113556.1.4.803:=65536)'` |
| `DONT_REQ_PREAUTH` | `0x400000` | Kerberos Pre-Auth Disabled. | `Get-DomainUser -PreauthNotRequired` |
| `TRUSTED_FOR_DELEGATION` | `0x80000` | Unconstrained Delegation. | `Get-DomainUser -Unconstrained` |
| `TRUSTED_TO_AUTH_FOR_DELEGATION` | `0x1000000` | Constrained Delegation. | `Get-DomainUser -TrustedToAuth` |

---

## 4. Domain Group & Membership Enumeration

| Command | Description |
| :--- | :--- |
| `Get-DomainGroup` | List all groups in the domain. |
| `Get-DomainGroup -Identity "<group>"` | View detailed properties for a specific domain group. |
| `Get-DomainGroupMember -Identity "<group>"` | List members of a specific domain group. |
| `Get-DomainGroupMember -Identity "Domain Admins" -Recurse` | Recursively list direct and nested members of Domain Admins. |
| `Get-DomainGroup -MemberIdentity <user>` | List all domain groups a specific user belongs to. |
| `Get-DomainForeignGroupMember` | Find members of local groups that originate from trusted foreign domains. |
| `Get-DomainForeignUser` | List foreign users explicitly granted access or memberships. |

---

## 5. Local Host, Group & Session Enumeration

*(Use these commands when inspecting local accounts/groups on a target host such as WS01)*

### PowerView Local Commands (Remote / Network Scope)

| Command | Description |
| :--- | :--- |
| `Get-NetLocalGroup -ComputerName <target>` | List local groups on a remote machine. |
| `Get-NetLocalGroupMember -ComputerName <target> -GroupName "<group>"` | List members of a specific local group on a host (e.g., "Remote Management Users"). |
| `Get-NetLoggedon -ComputerName <target>` | Query logged-on users on a remote machine. |
| `Get-NetSession -ComputerName <target>` | Query active SMB sessions on a remote host. |
| `Get-NetRDPSession -ComputerName <target>` | Query active RDP sessions on a remote host. |

### Native PowerShell & Net Commands (Local System Scope)

| Command | Description |
| :--- | :--- |
| `Get-LocalGroup` | List all local groups on the current host. |
| `Get-LocalGroupMember -Group "<group>"` | List members of a local group on the current host. |
| `Get-LocalUser` | List all local user accounts on the current host. |
| `net localgroup "<group>"` | Quick legacy command to view local group members. |

---

## 6. Computers, Shares & LAPS

| Command | Description |
| :--- | :--- |
| `Get-DomainComputer` | List all computer objects in the domain. |
| `Get-DomainComputer -OperatingSystem "*Server*"` | Filter domain computers by operating system. |
| `Get-DomainComputer -Unconstrained` | Find computers with Unconstrained Kerberos Delegation. |
| `Find-DomainShare` | Enumerate accessible SMB network shares across domain machines. |
| `Find-DomainShare -CheckShareAccess` | Verify read/write access permissions on discovered shares. |
| `Get-DomainUserEvent` | Query event logs on DCs to identify active user logon sessions. |
| `Get-DomainLAPSProperty` | Read LAPS passwords (if account has necessary permissions). |

---

## 7. Organizational Units (OUs) & Group Policy (GPOs)

| Command | Description |
| :--- | :--- |
| `Get-DomainOU` | List all Organizational Units in the domain. |
| `Get-DomainOU -Identity "<OU_Name>"` | Retrieve details for a specific Organizational Unit. |
| `(Get-DomainUser -SearchBase "OU=<OU>,DC=<domain>").Count` | Count total users within a specific OU. |
| `Get-DomainGPO` | List all Group Policy Objects (GPOs). |
| `Get-DomainGPOLocalGroup` | Query GPO settings that modify local group memberships. |

---

## 8. Kerberos Delegation Enumeration

| Delegation Type | PowerView Enumeration Command | Attack / Security Context |
| :--- | :--- | :--- |
| **Unconstrained** | `Get-DomainUser -Unconstrained`<br>`Get-DomainComputer -Unconstrained` | Account stores TGTs of users authenticating to it. |
| **Constrained (Protocol Transition)** | `Get-DomainUser -TrustedToAuth`<br>`Get-DomainComputer -TrustedToAuth` | Service can impersonate any user to specified target SPNs via S4U2Self/S4U2Proxy. |
| **Constrained (AllowedToDelegate)** | `Get-DomainUser -LDAPFilter "(msDS-AllowedToDelegateTo=*)"` | Lists target SPNs an account is authorized to delegate to. |
| **Resource-Based (RBCD)** | `Get-DomainComputer -LDAPFilter "(msDS-AllowedToActOnBehalfOfOtherIdentity=*)"` | Machine allows specified security principals to configure delegation against it. |

---

## 9. Active Directory ACLs & Rights Enumeration

### Critical Abusable Access Rights

* `GenericAll`: Full control over the target object.
* `GenericWrite` / `WriteProperty`: Ability to modify object attributes (e.g., reset passwords, add SPNs, set RBCD).
* `WriteDacl`: Ability to modify security permissions on the target object.
* `WriteOwner`: Ability to take ownership of the target object.
* `AllExtendedRights` / `ForceChangePassword`: Force password reset without knowing current password.
* `DS-Replication-Get-Changes` / `DS-Replication-Get-Changes-All`: **DCSync permissions** allowing domain credential dumping.

### ACL Enumeration Commands

| Command | Description |
| :--- | :--- |
| `Get-DomainObjectAcl -Identity <object>` | Retrieve DACL for a specific object. |
| `Get-DomainObjectAcl -Identity "Domain Admins" -ResolveGUIDs` | Retrieve DACL with human-readable rights and GUIDs. |
| `Find-InterestingDomainAcl -ResolveGUIDs` | Scan the domain for non-default or abusable ACL permissions. |
| `Get-DomainObjectAcl -SearchBase (Get-Domain).distinguishedName -ResolveGUIDs` | Query Domain Head ACLs to audit DCSync permissions. |

---

## 10. Balanced Scenario Playbooks

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
Get-DomainUser -LDAPFilter "(msDS-AllowedToDelegateTo=*)" | Select-Object samaccountname, msDS-AllowedToDelegateTo

```

### Playbook 5: Local Group & Host Enumeration

```powershell
# Query local group members on target host via PowerView
Get-NetLocalGroupMember -ComputerName WS01 -GroupName "Remote Management Users"

# Native PowerShell query directly on current host
Get-LocalGroupMember -Group "Remote Management Users"

```

### Playbook 6: DCSync Rights Hunting

```powershell
# Extract accounts holding DCSync (DS-Replication) permissions on Domain Head
Get-DomainObjectAcl -SearchBase (Get-Domain).distinguishedName -ResolveGUIDs | Where-Object {
    $_.ObjectAceType -match "DS-Replication-Get-Changes"
} | ForEach-Object {
    [PSCustomObject]@{
        Account = Convert-SidToName $_.SecurityIdentifier
        Right   = $_.ObjectAceType
    }
} | Select-Object Account, Right -Unique

```

---

## 11. Quick Command Summary Table

| Category | Primary PowerView Command |
| --- | --- |
| **Domain** | `Get-Domain`, `Get-DomainPolicyData`, `Get-DomainTrust`, `Get-ForestTrust` |
| **Users** | `Get-DomainUser`, `Get-DomainUser -SPN`, `Get-DomainUser -PreauthNotRequired` |
| **Domain Groups** | `Get-DomainGroup`, `Get-DomainGroupMember -Identity "Domain Admins" -Recurse` |
| **Local Groups** | `Get-NetLocalGroupMember -ComputerName WS01 -GroupName "<group>"`, `Get-LocalGroupMember` |
| **Computers** | `Get-DomainComputer`, `Get-DomainComputer -Unconstrained` |
| **Shares** | `Find-DomainShare -CheckShareAccess` |
| **OUs / GPOs** | `Get-DomainOU`, `Get-DomainGPO`, `Get-DomainGPOLocalGroup` |
| **ACLs / DCSync** | `Find-InterestingDomainAcl -ResolveGUIDs`, `Get-DomainObjectAcl` |

