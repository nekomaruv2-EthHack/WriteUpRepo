# ldapsearch Comprehensive Enumeration Cheat Sheet

> **DISCLAIMER & LEGAL NOTICE**
> This reference guide is strictly for educational purposes, security research, and authorized penetration testing within controlled lab environments or authorized engagements. Unauthorized scanning, enumeration, or querying of Directory Services without explicit written consent is illegal. Always perform these activities strictly within an authorized scope.

---

## 1. Syntax & Core Parameter Reference

The `ldapsearch` utility executes queries against LDAP/Active Directory servers. Mastering its command-line flags is critical for efficient enumeration.

### Basic Command Structure

```bash
ldapsearch -x -H ldap://<TARGET_IP> -D "<BIND_DN_OR_UPN>" -w "<PASSWORD>" -b "<BASE_DN>" "<LDAP_FILTER>" <ATTRIBUTES>
```

### Essential Parameter Reference

| Parameter | Description & Usage | Example |
| --- | --- | --- |
| `-x` | Use **Simple Authentication** (cleartext/basic bind) instead of SASL. | `ldapsearch -x ...` |
| `-H` | Target LDAP URI (`ldap://` or `ldaps://`). | `-H ldap://10.10.10.175` |
| `-b` | **Search Base** (Starting point DN in the directory tree). | `-b "DC=inlanefreight,DC=local"` |
| `-D` | **Bind DN / User Principal Name** used for authentication. | `-D "jdoe@inlanefreight.local"` or `-D "CN=jdoe,OU=Users,DC=domain,DC=local"` |
| `-w` | Supply Bind Password in plain text. | `-w 'Password123!'` |
| `-W` | Interactively prompt for Bind Password (prevents logging passwords in shell history). | `-W` |
| `-y` | Read Bind Password from a local file. | `-y pass.txt` |
| `-s` | **Search Scope**: `base` (object only), `one` (one level down), or `sub` (entire subtree, default). | `-s sub` |
| `-E` | Extended controls. **`-E pr=1000/noprompt`** enables LDAP Paging to bypass the AD 1,000-result query limit. | `-E pr=1000/noprompt` |
| `-LLL` | Suppress comment banners, LDAP version output, and printing of response headers. | `-LLL` |
| `-z` | Limit maximum number of search results returned. | `-z 50` |

---

## 2. Authentication Scenarios

### Anonymous Bind (Unauthenticated Search)

Query LDAP without credentials (allowed on legacy or misconfigured AD instances):

```bash
ldapsearch -x -H ldap://10.10.10.175 -b "DC=inlanefreight,DC=local"
```

### Authenticated Bind (Domain User Credentials)

Query using a domain user account:

```bash
ldapsearch -x -H ldap://10.10.10.175 -D "jdoe@inlanefreight.local" -w 'Password123!' -b "DC=inlanefreight,DC=local"
```

### SASL Authentication (NTLM / Kerberos)

Utilize NTLM or Kerberos mechanisms via SASL (does not use `-x`):

```bash
# NTLM Bind
ldapsearch -H ldap://dc01.inlanefreight.local -Y NTLM -U "jdoe" -b "DC=inlanefreight,DC=local"

# Kerberos Bind (Requires valid TGT in KRB5CCNAME)
ldapsearch -H ldap://dc01.inlanefreight.local -Y GSSAPI -b "DC=inlanefreight,DC=local"
```

---

## 3. Key Active Directory LDAP Attributes

When targeting specific information, restrict the query output by appending desired attributes to the end of your command:

| Category | Attribute Name | Description & Security Relevance |
| --- | --- | --- |
| **Identity** | `sAMAccountName` | User / Computer / Group account name. |
|  | `userPrincipalName` | UPN / Email-style identity (`user@domain.com`). |
|  | `distinguishedName` | Full LDAP path (`CN=...,OU=...,DC=...`). |
|  | `objectSid` | Binary Security Identifier of the object. |
| **Security Flags** | `userAccountControl` | Bitmask defining account states (disabled, pass never expires, etc.). |
| **Kerberos** | `servicePrincipalName` | SPNs attached to account (**Kerberoasting** targets). |
|  | `msDS-AllowedToDelegateTo` | Target SPNs for Constrained Delegation. |
|  | `msDS-AllowedToActOnBehalfOfOtherIdentity` | Binary descriptor for RBCD. |
| **Group / Membership** | `memberOf` | Groups this object belongs to. |
|  | `member` | Direct members of a group object. |
| **Management / LAPS** | `ms-Mcs-AdmPwd` | Legacy LAPS cleartext Administrator password. |
|  | `msLAPS-Password` | Modern LAPS password payload. |
| **Metadata** | `pwdLastSet` | Windows timestamp of last password change. |
|  | `lastLogonTimestamp` | Approximate last logon timestamp. |
|  | `adminCount` | Set to `1` for protected / high-privilege objects. |

---

## 4. LDAP Search Filters & OID Bitwise Operators

### Logical Operators

* **AND**: `(&(condition1)(condition2))`
* **OR**: `(|(condition1)(condition2))`
* **NOT**: `(!(condition))`
* **Wildcard**: `(sAMAccountName=admin*)`

### Active Directory Matching Rule OIDs (Bitwise Logic)

Active Directory uses specific Object Identifiers (OIDs) to evaluate bitmasks (such as `userAccountControl`) and transitive memberships directly within LDAP filters:

| Extensible Match OID | Name | Description |
| --- | --- | --- |
| `1.2.840.113556.1.4.803` | `LDAP_MATCHING_RULE_BIT_AND` | Evaluates if **all** specified bits are set in the attribute bitmask. |
| `1.2.840.113556.1.4.804` | `LDAP_MATCHING_RULE_BIT_OR` | Evaluates if **any** of the specified bits are set in the attribute bitmask. |
| `1.2.840.113556.1.4.1941` | `LDAP_MATCHING_RULE_IN_CHAIN` | Performs a **recursive / transitive** group membership lookup. |

---

## 5. Enumeration Playbooks

### Playbook 1: Domain Reconnaissance & RootDSE Query

* **Step 1: Discover Naming Contexts & Domain Information**
```bash
ldapsearch -x -H ldap://10.10.10.175 -s base -b "" namingContexts defaultNamingContext subschemaSubentry
```



---

### Playbook 2: User Account & Hash Hunting

* **Step 1: Enumerate All User Accounts (Filter out Computer Objects)**
```bash
ldapsearch -x -H ldap://10.10.10.175 -D "jdoe@inlanefreight.local" -w 'Password123!' \
  -b "DC=inlanefreight,DC=local" -E pr=1000/noprompt \
  "(&(objectCategory=person)(objectClass=user))" sAMAccountName userPrincipalName description
```


* **Step 2: Find Kerberoastable Accounts (Accounts with SPNs)**
```bash
ldapsearch -x -H ldap://10.10.10.175 -D "jdoe@inlanefreight.local" -w 'Password123!' \
  -b "DC=inlanefreight,DC=local" -E pr=1000/noprompt \
  "(&(objectCategory=person)(objectClass=user)(servicePrincipalName=*)(!(sAMAccountName=krbtgt)))" \
  sAMAccountName servicePrincipalName
```


* **Step 3: Find AS-REP Roastable Accounts (DONT_REQ_PREAUTH = 0x400000 / 4194304)**
```bash
ldapsearch -x -H ldap://10.10.10.175 -D "jdoe@inlanefreight.local" -w 'Password123!' \
  -b "DC=inlanefreight,DC=local" -E pr=1000/noprompt \
  "(&(objectCategory=person)(objectClass=user)(userAccountControl:1.2.840.113556.1.4.803:=4194304))" \
  sAMAccountName userAccountControl
```


* **Step 4: Find Accounts with "Password Never Expires" (DONT_EXPIRE_PASSWORD = 0x10000 / 65536)**
```bash
ldapsearch -x -H ldap://10.10.10.175 -D "jdoe@inlanefreight.local" -w 'Password123!' \
  -b "DC=inlanefreight,DC=local" -E pr=1000/noprompt \
  "(&(objectCategory=person)(objectClass=user)(userAccountControl:1.2.840.113556.1.4.803:=65536))" \
  sAMAccountName
```



---

### Playbook 3: Group & Privileged Membership Enumeration

* **Step 1: Enumerate All Domain Groups**
```bash
ldapsearch -x -H ldap://10.10.10.175 -D "jdoe@inlanefreight.local" -w 'Password123!' \
  -b "DC=inlanefreight,DC=local" -E pr=1000/noprompt \
  "(objectCategory=group)" sAMAccountName description
```


* **Step 2: List Direct Members of "Domain Admins"**
```bash
ldapsearch -x -H ldap://10.10.10.175 -D "jdoe@inlanefreight.local" -w 'Password123!' \
  -b "DC=inlanefreight,DC=local" \
  "(&(objectCategory=group)(sAMAccountName=Domain Admins))" member
```


* **Step 3: Recursively List All Members (Direct & Nested) of "Domain Admins"**
```bash
ldapsearch -x -H ldap://10.10.10.175 -D "jdoe@inlanefreight.local" -w 'Password123!' \
  -b "DC=inlanefreight,DC=local" -E pr=1000/noprompt \
  "(memberOf:1.2.840.113556.1.4.1941:=CN=Domain Admins,CN=Users,DC=inlanefreight,DC=local)" \
  sAMAccountName
```



---

### Playbook 4: Computer & Controller Enumeration

* **Step 1: Enumerate All Computer Objects & Operating Systems**
```bash
ldapsearch -x -H ldap://10.10.10.175 -D "jdoe@inlanefreight.local" -w 'Password123!' \
  -b "DC=inlanefreight,DC=local" -E pr=1000/noprompt \
  "(objectClass=computer)" dNSHostName operatingSystem operatingSystemVersion
```


* **Step 2: Identify Domain Controllers (SERVER_TRUST_ACCOUNT = 0x2000 / 8192)**
```bash
ldapsearch -x -H ldap://10.10.10.175 -D "jdoe@inlanefreight.local" -w 'Password123!' \
  -b "DC=inlanefreight,DC=local" \
  "(&(objectClass=computer)(userAccountControl:1.2.840.113556.1.4.803:=8192))" dNSHostName
```



---

### Playbook 5: Kerberos Delegation & LAPS Enumeration

* **Step 1: Find Unconstrained Delegation Systems (TRUSTED_FOR_DELEGATION = 0x80000 / 524288)**
```bash
ldapsearch -x -H ldap://10.10.10.175 -D "jdoe@inlanefreight.local" -w 'Password123!' \
  -b "DC=inlanefreight,DC=local" \
  "(&(userAccountControl:1.2.840.113556.1.4.803:=524288)(!(primaryGroupID=516)))" \
  sAMAccountName dNSHostName
```


* **Step 2: Find Constrained Delegation Accounts**
```bash
ldapsearch -x -H ldap://10.10.10.175 -D "jdoe@inlanefreight.local" -w 'Password123!' \
  -b "DC=inlanefreight,DC=local" \
  "(msDS-AllowedToDelegateTo=*)" \
  sAMAccountName msDS-AllowedToDelegateTo
```


* **Step 3: Dump LAPS Cleartext Passwords**
```bash
# Legacy LAPS
ldapsearch -x -H ldap://10.10.10.175 -D "jdoe@inlanefreight.local" -w 'Password123!' \
  -b "DC=inlanefreight,DC=local" \
  "(ms-Mcs-AdmPwd=*)" ms-Mcs-AdmPwd sAMAccountName

# Modern Windows LAPS
ldapsearch -x -H ldap://10.10.10.175 -D "jdoe@inlanefreight.local" -w 'Password123!' \
  -b "DC=inlanefreight,DC=local" \
  "(msLAPS-Password=*)" msLAPS-Password sAMAccountName
```



---

### Playbook 6: Output Parsing & Pipe Combinations

* **Step 1: Extract Clean List of Account Names**
```bash
ldapsearch -x -H ldap://10.10.10.175 -D "jdoe@inlanefreight.local" -w 'Password123!' \
  -b "DC=inlanefreight,DC=local" -E pr=1000/noprompt -LLL \
  "(&(objectCategory=person)(objectClass=user))" sAMAccountName | \
  grep -i "sAMAccountName:" | awk '{print $2}' | sort -u > users.txt
```



---

## 6. Quick Command Summary Table

| Goal / Target | Key Filter / Command Snippet |
| --- | --- |
| **RootDSE Info** | `-s base -b "" namingContexts` |
| **All Users** | `"(&(objectCategory=person)(objectClass=user))"` |
| **Kerberoasting** | `"(&(objectClass=user)(servicePrincipalName=*))"` |
| **AS-REP Roasting** | `"(userAccountControl:1.2.840.113556.1.4.803:=4194304)"` |
| **Pass Never Expires** | `"(userAccountControl:1.2.840.113556.1.4.803:=65536)"` |
| **Disabled Accounts** | `"(userAccountControl:1.2.840.113556.1.4.803:=2)"` |
| **Domain Admins** | `"(&(objectCategory=group)(sAMAccountName=Domain Admins))"` |
| **Nested Members** | `"(memberOf:1.2.840.113556.1.4.1941:=<GROUP_DN>)"` |
| **Unconstrained** | `"(userAccountControl:1.2.840.113556.1.4.803:=524288)"` |
| **Constrained** | `"(msDS-AllowedToDelegateTo=*)"` |
| **LAPS Passwords** | `"(ms-Mcs-AdmPwd=*)"` |