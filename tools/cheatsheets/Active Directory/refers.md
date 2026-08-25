### 1. Tools & Attack Vectors Reference Links

*   **Kerbrute**
    *   **概要**: Kerberos事前認証の仕組みを利用して、高速にドメインユーザーの列挙（User Enumeration）やパスワードスプレーを行うツール。
    *   **URL**: [https://github.com/ropnop/kerbrute](https://github.com/ropnop/kerbrute)
    *   **リリース (コンパイル済みバイナリ)**: [https://github.com/ropnop/kerbrute/releases/tag/v1.0.3](https://github.com/ropnop/kerbrute/releases/tag/v1.0.3)

*   **Inveigh**
    *   **概要**: PowerShell または C# で書かれた、Windowsマシン上で直接動作するクロスプラットフォームの中間者攻撃（MitM）およびポイズニング（スプーフィング）プラットフォーム。
    *   **URL**: [https://github.com/Kevin-Robertson/Inveigh](https://github.com/Kevin-Robertson/Inveigh)

*   **CrackMapExec (CME) / NetExec (NXC)**
    *   **概要**: SMBやLDAPを含む多数のプロトコルに対応し、パスワードポリシーの列挙やログインユーザーの探索、共有フォルダの自動巡回等を行うポストエクスプロイトツール。
    *   **URL (CrackMapExec)**: [https://github.com/byt3bl33d3r/CrackMapExec](https://github.com/byt3bl33d3r/CrackMapExec)
    *   **NetExec Wiki (Impersonate Logged-on Users)**: [https://www.netexec.wiki/smb-protocol/impersonate-logged-on-users](https://www.netexec.wiki/smb-protocol/impersonate-logged-on-users)

*   **enum4linux-ng**
    *   **概要**: WindowsやSambaから情報を列挙するPython製ツール。
    *   **URL**: [https://github.com/cddmp/enum4linux-ng](https://github.com/cddmp/enum4linux-ng)

*   **windapsearch**
    *   **概要**: LDAPクエリを利用して、Windowsドメインからユーザー、グループ、コンピューターなどの情報を列挙するPythonスクリプト。
    *   **URL**: [https://github.com/ropnop/windapsearch](https://github.com/ropnop/windapsearch)

*   **BloodHound.py**
    *   **概要**: 有効な資格情報を用いてLinux攻撃ホストからActive Directoryを巡回し、BloodHound GUI向けのデータを収集するPython製コレクター。
    *   **URL**: [https://github.com/dirkjanm/BloodHound.py](https://github.com/dirkjanm/BloodHound.py)

*   **Impacket Toolkit**
    *   **概要**: Windowsプロトコルを操作・悪用するPythonライブラリ群。リモート実行は用途で選択：`ADMIN$`へのバイナリ配置による標準RCEは`psexec.py`、バイナリ不使用で静かなSMB/MSRPC実行は`smbexec.py`、タスクスケジューラ経由の指定時刻実行（要時刻同期）は`atexec.py`、非対話的なサービス作成・管理は`services.py`を使用。その他`wmiexec.py`（WMIシェル）、`GetUserSPNs.py`（Kerberoasting）、`lookupsid.py`（SID列挙）、`ticketer.py`（チケット作成）、`raiseChild.py`（ドメイン昇格）、`mssqlclient.py`（MSSQL操作）等を収録。
    *   **psexec.py**: [https://github.com/fortra/impacket/blob/master/examples/psexec.py](https://github.com/fortra/impacket/blob/master/examples/psexec.py)
    *   **smbexec.py**: [https://github.com/fortra/impacket/blob/master/examples/smbexec.py](https://github.com/fortra/impacket/blob/master/examples/smbexec.py)
    *   **atexec.py**: [https://github.com/fortra/impacket/blob/master/examples/atexec.py](https://github.com/fortra/impacket/blob/master/examples/atexec.py)
    *   **services.py**: [https://github.com/fortra/impacket/blob/master/examples/services.py](https://github.com/fortra/impacket/blob/master/examples/services.py)
    *   **wmiexec.py**: [https://github.com/fortra/impacket/blob/master/examples/wmiexec.py](https://github.com/fortra/impacket/blob/master/examples/wmiexec.py)
    *   **GetUserSPNs.py**: [https://github.com/fortra/impacket/blob/master/examples/GetUserSPNs.py](https://github.com/fortra/impacket/blob/master/examples/GetUserSPNs.py)
    *   **lookupsid.py**: [https://github.com/fortra/impacket/blob/master/examples/lookupsid.py](https://github.com/fortra/impacket/blob/master/examples/lookupsid.py)
    *   **ticketer.py**: [https://github.com/fortra/impacket/blob/master/examples/ticketer.py](https://github.com/fortra/impacket/blob/master/examples/ticketer.py)
    *   **raiseChild.py**: [https://github.com/fortra/impacket/blob/master/examples/raiseChild.py](https://github.com/fortra/impacket/blob/master/examples/raiseChild.py)
    *   **mssqlclient.py**: [https://github.com/fortra/impacket/blob/master/examples/mssqlclient.py](https://github.com/fortra/impacket/blob/master/examples/mssqlclient.py)

*   **Snaffler**
    *   **概要**: Active Directory環境内のSMB共有を巡回し、認証情報や機密データが含まれるファイルを自動検出する監査ツール。
    *   **URL**: [https://github.com/SnaffCon/Snaffler](https://github.com/SnaffCon/Snaffler)

*   **Mimikatz**
    *   **概要**: メモリ（LSASS）から認証情報を抽出したり、Kerberosチケットのインジェクション・作成等を行うポストエクスプロイト用の有名ツール。
    *   **URL (ParrotSecによるFork版)**: [https://github.com/ParrotSec/mimikatz](https://github.com/ParrotSec/mimikatz)

*   **Rubeus**
    *   **概要**: Windows環境下において、Kerberos関連の攻撃（チケットの要求、Kerberoasting、AS-REP Roasting等）を柔軟に行うためのC#製ツール。
    *   **URL**: [https://github.com/GhostPack/Rubeus](https://github.com/GhostPack/Rubeus)

*   **JuicyPotato, PrintSpoofer, RoguePotato**
    *   **概要**: Windows環境において `SeImpersonatePrivilege` などの特権トークンを悪用してSYSTEM権限へ昇格するツール群。
    *   **JuicyPotato**: [https://github.com/ohpe/juicy-potato](https://github.com/ohpe/juicy-potato)
    *   **PrintSpoofer**: [https://github.com/itm4n/PrintSpoofer](https://github.com/itm4n/PrintSpoofer)
    *   **RoguePotato**: [https://github.com/antonioCoco/RoguePotato](https://github.com/antonioCoco/RoguePotato)

*   **noPac (SamAccountName スプーフィング)**
    *   **概要**: ドメインコントローラーへの権限昇格を可能にする2つの脆弱性 (CVE-2021-42278 および CVE-2021-42287) のPoC。
    *   **URL**: [https://github.com/Ridter/noPac](https://github.com/Ridter/noPac)

*   **PrintNightmare エクスプロイト**
    *   **概要**: Print Spoolerサービス（MS-RPRN）の欠陥を悪用し、リモートからSYSTEM権限で任意のDLLをロードさせてコードを実行させる脆弱性 (CVE-2021-1675 / CVE-2021-2675) のPoC。
    *   **CVE-2021-1675 (cube0x0)**: [https://github.com/cube0x0/CVE-2021-1675.git](https://github.com/cube0x0/CVE-2021-1675.git)
    *   **Impacket (cube0x0 Fork版)**: [https://github.com/cube0x0/impacket](https://github.com/cube0x0/impacket)

*   **PKINITtools**
    *   **概要**: AD CS（Active Directory 証明書サービス）を中継した後のPKINITステージにおいて、取得した証明書をもとにTGTの要求を行うツール群。
    *   **URL**: [https://github.com/dirkjanm/PKINITtools](https://github.com/dirkjanm/PKINITtools)

*   **Certi**
    *   **概要**: AD CS関連の設定をダンプ・列挙するPython製ツール。
    *   **URL**: [https://github.com/zer1t0/certi](https://github.com/zer1t0/certi)

*   **PetitPotam**
    *   **概要**: MS-EFSRPCプロトコルを悪用し、ドメインコントローラー等のホストに対して、攻撃者が指定したホストへNTLM接続を強制させる脆弱性 (CVE-2021-36942) のPoC。
    *   **URL**: [https://github.com/topotam/PetitPotam](https://github.com/topotam/PetitPotam)

*   **Printer Bug 検出・活用ツール**
    *   **概要**: MS-RPRNを利用した強制認証（Printer Bug）が可能かどうかをチェック、あるいは攻撃を自動化するスクリプト群。
    *   **Security-Assessment-PS**: [https://github.com/itzvenom/Security-Assessment-PS](https://github.com/itzvenom/Security-Assessment-PS)
    *   **NetNTLMtoSilverTicket**: [https://github.com/NotMedic/NetNTLMtoSilverTicket](https://github.com/NotMedic/NetNTLMtoSilverTicket)

*   **PyKEK (MS14-068 エクスプロイト)**
    *   **概要**: KerberosのPAC署名不備を悪用し、標準ユーザーをドメイン管理者として偽装するエクスプロイトツール。
    *   **URL**: [https://github.com/SecWiki/windows-kernel-exploits/tree/master/MS14-068/pykek](https://github.com/SecWiki/windows-kernel-exploits/tree/master/MS14-068/pykek)

*   **adidnsdump**
    *   **概要**: Active Directory 統合DNS（ADIDNS）からDNSレコード情報を一括で列挙・エクスポートするPythonツール。
    *   **URL**: [https://github.com/dirkjanm/adidnsdump](https://github.com/dirkjanm/adidnsdump)
    *   **開発者ブログ解説**: [https://dirkjanm.io/getting-in-the-zone-dumping-active-directory-dns-with-adidnsdump/](https://dirkjanm.io/getting-in-the-zone-dumping-active-directory-dns-with-adidnsdump/)

*   **GPOセキュリティ監査ツール**
    *   **概要**: GPO（グループポリシーオブジェクト）の不適切な設定や脆弱性を分析・報告する各種ツール。
    *   **Group3r**: [https://github.com/Group3r/Group3r](https://github.com/Group3r/Group3r)
    *   **ADRecon**: [https://github.com/sense-of-security/ADRecon](https://github.com/sense-of-security/ADRecon)
    *   **PingCastle**: [https://www.pingcastle.com/](https://www.pingcastle.com/)
    *   **SharpGPOAbuse**: [https://github.com/ReversecLabs/SharpGPOAbuse](https://github.com/ReversecLabs/SharpGPOAbuse)

---

### 2. PowerShell 管理・状況把握ツール (PowerShell & Policy Administration Tools)

*   **PowerView / PowerSploit**
    *   **概要**: Active Directory環境下での状況認識（Situational Awareness）に幅広く活用される、PowerShell製の主要AD探索フレームワーク。
    *   **GitHub**: [https://github.com/PowerShellMafia/PowerSploit/tree/master/Recon](https://github.com/PowerShellMafia/PowerSploit/tree/master/Recon)
    *   **公式ドキュメント**: [https://powersploit.readthedocs.io/en/latest/](https://powersploit.readthedocs.io/en/latest/)
    *   **Test-AdminAccess**: [https://powersploit.readthedocs.io/en/latest/Recon/Test-AdminAccess/](https://powersploit.readthedocs.io/en/latest/Recon/Test-AdminAccess/)
    *   **Set-DomainUserPassword**: [https://powersploit.readthedocs.io/en/latest/Recon/Set-DomainUserPassword/](https://powersploit.readthedocs.io/en/latest/Recon/Set-DomainUserPassword/)

*   **BC-Security PowerView (Empire 4)**
    *   **概要**: 本来非推奨となった元のPowerSploitパッケージから、BC-Securityにより最新アップデートがメンテナンスされているバージョン。
    *   **URL**: [https://github.com/BC-SECURITY/Empire/blob/main/empire/server/data/module_source/situational_awareness/network/powerview.ps1](https://github.com/BC-SECURITY/Empire/blob/main/empire/server/data/module_source/situational_awareness/network/powerview.ps1)

---

### 3. Microsoft公式＆規格参考URL (Microsoft & Industry Standard Reference Links)

*   **Samba/enum4linux マニュアル**: [https://www.samba.org/samba/docs/current/man-html/samba.7.html](https://www.samba.org/samba/docs/current/man-html/samba.7.html)
*   **rpcclient マニュアル**: [https://www.samba.org/samba/docs/current/man-html/rpcclient.1.html](https://www.samba.org/samba/docs/current/man-html/rpcclient.1.html)
*   **LLMNR規格 (RFC 4795)**: [https://datatracker.ietf.org/doc/html/rfc4795](https://datatracker.ietf.org/doc/html/rfc4795)
*   **NBT-NS (NetBIOS Name Service) 関連ドキュメント**: [https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-2000-server/cc940063(v=technet.10)?redirectedfrom=MSDN](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-2000-server/cc940063(v=technet.10)?redirectedfrom=MSDN)
*   **Windows セキュリティ識別子 (SID) の理解**: [https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/understand-security-identifiers](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/understand-security-identifiers)
*   **Windows Management Instrumentation (WMI) スタートページ**: [https://learn.microsoft.com/en-us/windows/win32/wmisdk/wmi-start-page](https://learn.microsoft.com/en-us/windows/win32/wmisdk/wmi-start-page)
*   **WMI概要**: [https://learn.microsoft.com/en-us/windows/win32/wmisdk/about-wmi](https://learn.microsoft.com/en-us/windows/win32/wmisdk/about-wmi)
*   **BloodHound Edges (例: CanRDP)**: [https://bloodhound.specterops.io/resources/edges/can-rdp](https://bloodhound.specterops.io/resources/edges/can-rdp)
*   **Active Directory PowerShell モジュール (General)**: [https://learn.microsoft.com/en-us/powershell/module/activedirectory/](https://learn.microsoft.com/en-us/powershell/module/activedirectory/)
*   **Active Directory PowerShell モジュール (Get-ADUser)**: [https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-aduser?view=windowsserver2022-ps](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-aduser?view=windowsserver2022-ps)
*   **Microsoft.PowerShell.Core モジュール**: [https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/?view=powershell-7.6&viewFallbackFrom=powershell-7.2](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/?view=powershell-7.6&viewFallbackFrom=powershell-7.2)
*   **Get-Module コマンドレット**: [https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/get-module?view=powershell-7.6&viewFallbackFrom=powershell-7.2](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/get-module?view=powershell-7.6&viewFallbackFrom=powershell-7.2)
*   **PowerShell モジュール一覧**: [https://learn.microsoft.com/en-us/powershell/module/](https://learn.microsoft.com/en-us/powershell/module/)
*   **WMIC コマンドチートシート (Gist)**: [https://gist.github.com/xorrior/67ee741af08cb1fc86511047550cdaf4](https://gist.github.com/xorrior/67ee741af08cb1fc86511047550cdaf4)
*   **Windows コマンドラインツール - netsh**: [https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/netsh](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/netsh)
*   **Windows コマンドラインツール - sc-query**: [https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/sc-query](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/sc-query)
*   **Dsquery コマンドレファンス**: [https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/cc754232(v=ws.11)](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/cc754232(v=ws.11))
*   **UserAccountControl（UAC）属性の制御**: [https://learn.microsoft.com/en-us/troubleshoot/windows-server/active-directory/useraccountcontrol-manipulate-account-properties](https://learn.microsoft.com/en-us/troubleshoot/windows-server/active-directory/useraccountcontrol-manipulate-account-properties)
*   **LDAP 一致ルール (Matching Rules) の仕様**: [https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-adts/4e638665-f466-4597-93c4-12f2ebfabab5](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-adts/4e638665-f466-4597-93c4-12f2ebfabab5)
*   **.NET SecureString クラス概要**: [https://learn.microsoft.com/en-us/dotnet/api/system.security.securestring?view=net-6.0](https://learn.microsoft.com/en-us/dotnet/api/system.security.securestring?view=net-6.0)
*   **Microsoft Security ブログ - SamAccountName スプーフィング**: [https://techcommunity.microsoft.com/blog/microsoft-security-blog/sam-name-impersonation/3042699](https://techcommunity.microsoft.com/blog/microsoft-security-blog/sam-name-impersonation/3042699)
*   **Sophos ブログ - noPac 脆弱性の恐怖**: [https://www.sophos.com/en-us/blog/nopac-a-tale-of-two-vulnerabilities-that-could-end-in-ransomware](https://www.sophos.com/en-us/blog/nopac-a-tale-of-two-vulnerabilities-that-could-end-in-ransomware)
*   **AD Security - Windowsドメインの既知のSIDリスト**: [https://adsecurity.org/?p=1001](https://adsecurity.org/?p=1001)
*   **Windows コマンドラインツール - runas**: [https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/cc771525(v=ws.11)](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/cc771525(v=ws.11))