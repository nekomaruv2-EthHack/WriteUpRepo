# MySQL コマンドチートシート (MySQL Command Cheat Sheet)

## 1. 接続 (Connection)
* **ローカル接続:** `mysql -u root -p`
* **ホスト指定で接続:** `mysql -h <host> -u <username> -p`
* **ポート指定で接続:** `mysql -h <host> -P 3306 -u <username> -p`
* **クエリを直接実行:** `mysql -u <username> -p -e "SHOW DATABASES;"`

## 2. 基本情報・メタデータ取得 (Information Gathering)
* **バージョン確認:** `SELECT VERSION();` または `SHOW VARIABLES LIKE 'version';`
* **現在実行中のユーザー:** `SELECT USER();` または `SELECT CURRENT_USER();`
* **現在のデータベース:** `SELECT DATABASE();`
* **ホスト名:** `SELECT @@hostname;`
* **データディレクトリの確認:** `SHOW VARIABLES LIKE 'datadir';`

## 3. データベース・テーブル操作 (Database & Table Operations)
* **データベース一覧:** `SHOW DATABASES;`
* **データベース作成:** `CREATE DATABASE <db_name> CHARACTER SET utf8mb4;`
* **データベース選択:** `USE <db_name>;`
* **テーブル一覧:** `SHOW TABLES;`
* **テーブル定義（カラム情報）確認:** `DESCRIBE <table_name>;` または `SHOW COLUMNS FROM <table_name>;`
* **テーブル作成SQLの確認:** `SHOW CREATE TABLE <table_name>\G`

## 4. ユーザー・権限管理 (User & Privilege Management)
* **ユーザー一覧:** `SELECT User, Host FROM mysql.user;`
* **ユーザー作成:** `CREATE USER '<username>'@'%' IDENTIFIED BY '<password>';`
* **権限付与:** `GRANT ALL PRIVILEGES ON <db_name>.* TO '<username>'@'%';`
* **権限の反映:** `FLUSH PRIVILEGES;`
* **自ユーザーの権限確認:** `SHOW GRANTS;`

## 5. ファイル読み書き・ペンテスト関連クエリ (File Operations & Useful Queries)
* **ファイルの内容をテーブルに読み込む:**
  ```sql
  LOAD DATA INFILE '/etc/passwd' INTO TABLE test_table FIELDS TERMINATED BY '\\n';
```
* **クエリ結果をファイルへ出力:**
```sql
SELECT * FROM users INTO OUTFILE '/var/www/html/output.txt';
```


* **全テーブルから特定カラムを検索（情報探索用）:**
```sql
SELECT table_schema, table_name, column_name 
FROM information_schema.columns 
WHERE column_name LIKE '%pass%';
```



## 6. チューニング・デバッグ (Tuning & Debugging)

* **プロセス一覧（実行中のクエリ）:** `SHOW PROCESSLIST;` または `SHOW FULL PROCESSLIST;`
* **クエリの実行計画確認:** `EXPLAIN SELECT * FROM <table_name> WHERE ...;`
* **スロークエリログの設定確認:** `SHOW VARIABLES LIKE 'slow_query_log';`
"""
with open("mysql_commands.md", "w", encoding="utf-8") as f:
f.write(md_content)

print("mysql_commands.md generated successfully.")
```

```text?code_stdout&code_event_index=1
mysql_commands.md generated successfully.
```
