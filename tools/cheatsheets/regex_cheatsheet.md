# Regular Expression Cheat Sheet

> **Linux / Bash / grep / sed / awk 向け・正規表現チートシート**  
> 正規表現の基本を網羅し、検索・抽出・置換・条件分岐をその場で書けるようにするためのリファレンス。  
> **基本は POSIX ERE（拡張正規表現）**。PCRE 固有の構文は別扱いにする。

**読み方**

- コード例は原則として **Bash 上で実行するコマンド**。ファイル名は置き換える。
- `grep -E`、`sed -E`、`awk`、Bash の `[[ =~ ]]` は基本的に **ERE** を使う。
- 通常の `grep` と `sed` の既定は **BRE**。記号の使い方が一部異なる。
- `grep -P` は GNU grep の **PCRE** オプション。環境によっては使用できない。
- `regex` と書いたブロックは正規表現自体を示す（シェルコマンドではない）。
- 数字や日付などのパターンは、別記がなければ**形式を調べるための例**であり、値の正当性を保証しない。

## Contents

1. [Quick Start](#1-quick-start)
2. [BRE / ERE / PCRE](#2-bre--ere--pcre)
3. [Special Characters](#3-special-characters)
4. [Character Classes](#4-character-classes)
5. [Anchors](#5-anchors)
6. [Quantifiers](#6-quantifiers)
7. [Grouping & Alternation](#7-grouping--alternation)
8. [Matching Rules](#8-matching-rules)
9. [grep](#9-grep)
10. [sed](#10-sed)
11. [awk](#11-awk)
12. [Bash `[[ =~ ]]`](#12-bash-regex)
13. [Regex vs Glob](#13-regex-vs-glob)
14. [Practical Patterns](#14-practical-patterns)
15. [PCRE Extensions](#15-pcre-extensions)
16. [Shell Quoting](#16-shell-quoting)
17. [find / ripgrep](#17-find--ripgrep)
18. [Exit Status](#18-exit-status)
19. [Testing](#19-testing)
20. [Common Pitfalls](#20-common-pitfalls)
21. [Quick Reference](#21-quick-reference)
22. [References](#22-references)

---

## 1. Quick Start

### 最初に覚える基本形

```bash
# ERE で行を検索
grep -E 'error|warning' app.log

# 一致部分だけ取り出す（GNU grep）
grep -oE '[0-9]+' app.log

# 置換する
sed -E 's/[[:space:]]+/ /g' input.txt

# Bash の条件分岐
value='user_123'
if [[ $value =~ ^[[:alnum:]_]+$ ]]; then
    echo 'Valid'
fi
```

### パターンの読み方

```regex
^([A-Za-z]+)[[:space:]]+([0-9]{2,4})$
```

**行頭 → 英字 1 文字以上 → 空白 1 文字以上 → 数字 2〜4 文字 → 行末**。

```text
Alice 123    # 一致
Bob 42       # 一致
Alice abc    # 不一致
X 12345      # 不一致
```

---

## 2. BRE / ERE / PCRE

**正規表現の書き方は、コマンドによって違う。** 特に `+`、`?`、`()`、`|` に注意。

| 種類 | 代表例 | 使い分け |
|---|---|---|
| BRE（基本正規表現） | `grep`、`sed`（既定） | `\(ab\)`、`\{2,4\}` |
| ERE（拡張正規表現） | `grep -E`、`sed -E`、`awk`、`[[ =~ ]]` | `(ab)`、`{2,4}`、`+`、`?` |
| PCRE（Perl 互換） | GNU `grep -P` など | `\d`、`\s`、`.*?`、先読みなど |
| 固定文字列検索 | `grep -F` | 正規表現を解釈せず探す |

### BRE と ERE の書き換え

| 機能 | BRE | ERE |
|---|---|---|
| 1 回以上 | `a\+`（GNU 拡張） | `a+` |
| 0 または 1 回 | `a\?`（GNU 拡張） | `a?` |
| 2〜4 回 | `a\{2,4\}` | `a{2,4}` |
| グループ | `\(ab\)` | `(ab)` |
| OR | <code>a\&#124;b</code>（GNU 拡張） | <code>a&#124;b</code> |

BRE の `\+`、`\?`、`\|` は **POSIX BRE 標準ではない**。通常は ERE に揃えるのがおすすめ。

```bash
grep -E '^(cat|dog)[0-9]+$' file.txt  # ERE
grep '^[0-9]*$' file.txt             # BRE（基本的な記法）
grep -F 'file.name' file.txt          # 固定文字列
```

**覚え方：検索は `grep -E`、置換は `sed -E` を基本にする。**

---

## 3. Special Characters

### 普通の文字と特殊な文字

```regex
hello         # hello の文字列
abc123        # abc123 の文字列
```

| ERE 記号 | 意味 |
|---|---|
| `.` | 任意の 1 文字（通常、改行を除く） |
| `^` / `$` | 行頭 / 行末 |
| `*` / `+` / `?` | 繰り返し回数 |
| `{m,n}` | m〜n 回の繰り返し |
| `[...]` | 文字集合 |
| `(...)` | グループ |
| <code>&#124;</code> | OR |
| `\` | エスケープ |

### `.` と `\.` の違い

```bash
printf '%s\n' 'a.b' 'axb' 'ab' | grep -E '^a.b$'
# a.b
# axb

printf '%s\n' 'a.b' 'axb' | grep -E '^a\.b$'
# a.b
```

```regex
\.        # ドット .
\*        # アスタリスク *
\+        # プラス +
\?        # クエスチョンマーク ?
\[        # 左角括弧 [
\(        # 左丸括弧 (
\$        # ドル記号 $
\\        # バックスラッシュ \
```

**注意：** `\` は正規表現だけでなくシェルにも意味がある。コマンド内では `'<regex>'` のようにシングルクォートを使うことが多い。

---

## 4. Character Classes

### `[...]`（1 文字を選ぶ）

```regex
[abc]         # a / b / c のいずれか
[a-z]         # a〜z の範囲（ロケールに注意）
[A-Z]         # A〜Z の範囲（ロケールに注意）
[0-9]         # 数字 1 文字
[A-Za-z0-9]   # ASCII 英数字を想定
[^abc]        # a / b / c 以外の 1 文字
[^0-9]        # 数字以外の 1 文字
[.]           # 文字としてのドット
```

`[^...]` の先頭 `^` は**否定**。角括弧の外側に置いた `^`（行頭）とは意味が違う。

### POSIX 文字クラス（実務でよく使う）

| 記法 | 意味 |
|---|---|
| `[[:digit:]]` | 数字 |
| `[[:alpha:]]` | アルファベット文字 |
| `[[:alnum:]]` | 文字または数字 |
| `[[:lower:]]` | 小文字 |
| `[[:upper:]]` | 大文字 |
| `[[:space:]]` | 空白（スペース、タブなど） |
| `[[:blank:]]` | 水平空白（スペース、タブ） |
| `[[:punct:]]` | 記号類 |
| `[[:xdigit:]]` | 16 進数字 |
| `[[:print:]]` | 印字可能文字（空白含む） |
| `[[:graph:]]` | 印字可能文字（空白除く） |

```bash
grep -E '[[:digit:]]' file.txt        # 数字を含む行
grep -E '^[[:digit:]]+$' file.txt     # 数字だけの行
grep -E '^$' file.txt               # 完全な空行
grep -E '^[[:space:]]*$' file.txt    # 空白だけの行も含む
```

**`[:digit:]` ではなく `[[:digit:]]`。** 外側の角括弧を忘れない。

### ロケールの注意

```bash
LC_ALL=C grep -E '^[A-Za-z0-9_]+$' names.txt
```

`LC_ALL=C` は ASCII 前提の扱いを明確にしたい場合に有用。大小文字・文字の範囲・単語境界などはロケールに左右されうる。

---

## 5. Anchors

| 記法 | 意味 |
|---|---|
| `^ERROR` | ERROR で始まる行 |
| `\.log$` | .log で終わる行 |
| `^[0-9]+$` | 行全体が数字 |
| `^$` | 完全な空行 |
| `^[[:space:]]*$` | 空行、または空白だけの行 |

```bash
grep -E '^ERROR' app.log
grep -E '\.conf$' files.txt
grep -E '^[0-9]+$' numbers.txt
```

`^` と `$` は文字ではなく**位置の指定**。部分一致を許容するか、行全体の一致が必要かで使い分ける。

### 単語単位（GNU grep）

```bash
grep -w 'cat' animals.txt    # 単語として cat に一致
grep -x 'cat' animals.txt    # 行全体が cat の場合だけ
```

---

## 6. Quantifiers

繰り返しの指定は**直前の文字・文字集合・グループ**にかかる（ERE）。

| 記法 | 意味 | 一致例 |
|---|---|---|
| `a*` | 0 回以上 | `b` に対して `a*` は空文字にも一致 |
| `a+` | 1 回以上 | `a`, `aaa` |
| `a?` | 0 または 1 回 | 空文字、`a` |
| `a{3}` | ちょうど 3 回 | `aaa` |
| `a{2,4}` | 2〜4 回 | `aa`, `aaa`, `aaaa` |
| `a{2,}` | 2 回以上 | `aa`, `aaaa` |
| `[0-9]+` | 数字が 1 文字以上 | `42`, `123` |
| `(ab)+` | ab を 1 回以上 | `ab`, `abab` |

### `*` と `+` の違い

```bash
printf '%s\n' 'bc' 'bac' 'baac' | grep -E '^ba*c$'
# bc
# bac
# baac

printf '%s\n' 'bc' 'bac' 'baac' | grep -E '^ba+c$'
# bac
# baac
```

`*` は **0 回でもよい**。`+` は **最低 1 回必要**。

### ちょうど 4 桁

```bash
printf '%s\n' '123' '1234' '12345' | grep -E '^[0-9]{4}$'
# 1234
```

### `.*` と `.+`

```regex
.*        # 任意の文字 0 文字以上（空でも可）
.+        # 任意の文字 1 文字以上
```

`.*` は意図より広く一致しやすい。可能なら `[^,]*`（カンマ以外）のように対象を絞る。

---

## 7. Grouping & Alternation

### OR / グループ

```bash
grep -E 'error|warning' app.log
printf '%s\n' 'yes' 'no' 'maybe' | grep -E '^(yes|no)$'
# yes
# no
```

```regex
(ab)+                 # ab が 1 回以上
https?                # http または https
(cat|dog)s?           # cat / cats / dog / dogs
^([0-9]{4})-([0-9]{2})-([0-9]{2})$  # 日付形式
```

```text
ab+       : a の後に b が 1 回以上
(ab)+     : ab という組み合わせが 1 回以上
```

### 優先順位

```regex
^cat|dog$       # cat で始まる OR dog で終わる
^(cat|dog)$     # 行全体が cat または dog
```

OR の対象は適切に `(...)` で囲む。

### キャプチャ（括弧内を再利用する）

```bash
printf '%s\n' '2026-11-02' | sed -E 's@^([0-9]{4})-([0-9]{2})-([0-9]{2})$@\1/\2/\3@'
# 2026/11/02
```

ここでは `\1` / `\2` / `\3` は**sed の置換側**で、1〜3 番目のグループを表す。

---
## 8. Matching Rules

### 部分一致が基本

```bash
printf '%s\n' 'an error occurred' | grep -E 'error'
# an error occurred
```

`grep` は**正規表現を含む行**を出力する。行全体が一致する必要はない。

### ERE の最長一致

```bash
printf '%s\n' '<a><b>' | grep -oE '<.*>'
# <a><b>
```

POSIX ERE では原則として左端の一致を選び、同じ位置から始まる候補の中では最長のものを選ぶ。

```bash
# '>' 以外の文字列を使えば区切りごとに抽出できる
printf '%s\n' '<a><b>' | grep -oE '<[^>]*>'
# <a>
# <b>
```

`<.*?>` のような**非貪欲**量指定は ERE では使えない（PCRE については第 15 章）。

---

## 9. grep

`grep` は**一致する行を探す**コマンド。

### 基本オプション

```bash
grep 'error' app.log                   # BRE で検索
grep -E 'error|warning' app.log        # ERE で検索
grep -F 'a.b' app.log                  # 固定文字列として検索
grep -i 'error' app.log                # 大文字・小文字を無視
grep -n 'error' app.log                # 行番号を表示
grep -v '^#' config.txt               # 一致しない行
grep -c 'error' app.log                # 一致する行数
grep -l 'error' ./*.log                # 一致するファイル名
grep -L 'error' ./*.log                # 一致しないファイル名
grep -w 'root' /etc/passwd            # 単語単位で一致
grep -x 'READY' status.txt            # 行全体が READY
grep -q 'READY' status.txt            # 出力せず終了コードで判定
```

`grep -c` はマッチした**回数**ではなく、マッチを含む**行数**を数える。

### 一致した行の前後を表示（GNU grep）

```bash
grep -n -A 3 'ERROR' app.log    # 後ろ 3 行
grep -n -B 2 'ERROR' app.log    # 前 2 行
grep -n -C 2 'ERROR' app.log    # 前後 2 行
```

### 一致箇所だけ抽出（GNU grep）

```bash
printf '%s\n' 'id=123 user=alice' | grep -oE '[0-9]+'
# 123

printf '%s\n' 'a=12 b=345' | grep -oE '[0-9]+'
# 12
# 345
```

### OR・AND・除外

```bash
grep -E 'error|warning|fatal' app.log        # OR
grep 'error' app.log | grep 'timeout'       # AND
grep -E 'error|warning' app.log | grep -v 'ignored'  # 除外
grep -e 'error' -e 'warning' app.log       # 複数パターンを指定
```

### ディレクトリを再帰的に検索（GNU grep）

```bash
grep -RnE 'TODO|FIXME' ./src
grep -Rn --include='*.py' 'TODO' ./src
grep -Rn --exclude='*.log' 'password' ./src
grep -Rn --exclude-dir='.git' 'TODO' .
```

`--include='*.py'` の `*.py` は**ファイル名 glob**であり、正規表現ではない。

### パターンがハイフンで始まる

```bash
grep -E -- '^-hello' file.txt
grep -e '-hello' file.txt
```

### 固定文字列を探すときは `-F`

```bash
keyword='a+b(c).txt'
grep -F -- "$keyword" file.txt
```

ユーザーから渡された文字列に `.` や `*` があっても文字どおり探せる。

---

## 10. sed

`sed` は**文字列の置換・加工**に使う。ここでは基本的に `-E`（ERE）を指定する。

### 基本置換

```bash
printf '%s\n' 'hello world' | sed -E 's/world/Linux/'
# hello Linux

printf '%s\n' 'a a a' | sed -E 's/a/X/g'
# X X X
```

`g` を省略すると**各行の最初の一致箇所だけ**置換する。

### よく使う置換

```bash
sed -E 's/[[:space:]]+/ /g' file.txt     # 連続空白を 1 個に
sed -E 's/^[[:space:]]+//' file.txt     # 行頭の空白を除去
sed -E 's/[[:space:]]+$//' file.txt     # 行末の空白を除去
sed -E 's/^/# /' file.txt              # 行頭に # を追加
sed -E 's/$/;/' file.txt               # 行末に ; を追加
sed -E 's/\.txt$/.md/' files.txt       # .txt を .md に
```

### キャプチャを使った置換

```bash
printf '%s\n' 'Alice Smith' | sed -E 's/^([^ ]+) ([^ ]+)$/\2, \1/'
# Smith, Alice
```

`\1`、`\2` はそれぞれ 1 番目と 2 番目の括弧で一致した文字列。

### `&` は一致全体

```bash
printf '%s\n' 'id=123' | sed -E 's/[0-9]+/[&]/g'
# id=[123]
```

`\1` はキャプチャ、`&` は**一致した全体**を置換側で参照する記号。

### 区切り文字の変更

```bash
printf '%s\n' '/usr/local/bin' | sed -E 's@/usr/local@/opt/tools@'
# /opt/tools/bin
```

`/` を含むパスなら `s@検索@置換@` のように区切り文字を変えると読みやすい。

### 条件に一致した行だけ置換

```bash
sed -E '/ERROR/s/foo/bar/g' app.log
```

### 一致した行だけ出す

```bash
sed -n -E '/^ERROR/p' app.log
sed -n '5,10p' file.txt                 # 5〜10 行目を出力
```

`-n` は自動出力を抑制し、`p` で必要な行だけ出力する。

### ファイルの直接編集

```bash
# 元ファイルは変えずに標準出力へ
sed -E 's/foo/bar/g' input.txt

# バックアップを残して編集（GNU / BSD sed）
sed -E -i.bak 's/foo/bar/g' input.txt
# input.txt.bak ができる
```

GNU / BSD の `-i` は引数の扱いが異なるため、まず `-i.bak` でバックアップを作るのが安全。

### BRE のまま使う場合

```bash
printf '%s\n' 'foo123' | sed 's/\(foo\)\([0-9]*\)/\2-\1/'
# 123-foo
```

BRE のグループは `\(...\)` になる。

---

## 11. awk

`awk` は**列を扱いながら検索・抽出・置換**するのが得意。正規表現は基本的に ERE。

### 正規表現で行を抽出

```bash
awk '/ERROR/' app.log
awk '/ERROR|WARN/' app.log
awk '!/DEBUG/' app.log
awk '/^[[:digit:]]+$/' numbers.txt
```

### `~` / `!~` による判定

```bash
awk '$0 ~ /error/' app.log        # 行全体を調べる
awk '$0 !~ /debug/' app.log       # 一致しない行
awk '$1 ~ /^[A-Z]/' data.txt     # 1 列目で判定
```

### 列を使った処理

```bash
awk '{print $1, $3}' data.txt                  # 空白区切りで列を出力
awk -F: '{print $1}' /etc/passwd              # : 区切り
awk '$2 ~ /^[0-9]+$/ {print $1}' data.txt     # 2 列目が数字なら 1 列目
```

`$0` は行全体、`$1` は 1 列目、`$2` は 2 列目。`-F:` は入力列の区切りを `:` にする。

### AND 条件

```bash
awk '$1 == "admin" && $2 ~ /^[0-9]+$/ {print $0}' data.txt
```

### `sub` / `gsub`

```bash
printf '%s\n' 'a12 b34' | awk '{sub(/[0-9]+/, "N"); print}'
# aN b34

printf '%s\n' 'a12 b34' | awk '{gsub(/[0-9]+/, "N"); print}'
# aN bN
```

- `sub(regex, replacement, target)`：最初の 1 箇所。
- `gsub(regex, replacement, target)`：すべての箇所。
- `target` を省略すると `$0` が対象。

### `match` / `RSTART` / `RLENGTH`

```bash
printf '%s\n' 'user=alice id=42' | awk '
    match($0, /id=[0-9]+/) {
        print substr($0, RSTART, RLENGTH)
    }
'
# id=42
```

`match` は開始位置を `RSTART`、長さを `RLENGTH` に設定する。**POSIX awk はキャプチャ配列を標準では提供しない**。

### Bash 変数からパターンを渡す

```bash
word='ERROR|WARN'
awk -v pattern="$word" '$0 ~ pattern' app.log
```

`$0 ~ pattern` は文字列変数を正規表現として評価する。

---

## 12. Bash Regex

Bash の `[[ 文字列 =~ 正規表現 ]]` では ERE を使用する。

### 基本

```bash
value='abc123'
if [[ $value =~ ^[a-z]+[0-9]+$ ]]; then
    echo 'match'
fi
```

`=~` は部分一致。**文字列全体の確認には `^...$` を使う。**

### よくあるパターン

```bash
status='warning'
[[ $status =~ ^(ok|warning|error)$ ]] && echo 'known status'

id='12345'
[[ $id =~ ^[0-9]+$ ]] && echo 'digits only'

date='2026-11-02'
[[ $date =~ ^[0-9]{4}-[0-9]{2}-[0-9]{2}$ ]] && echo 'date-shaped'
```

### キャプチャ：`BASH_REMATCH`

```bash
line='user=alice id=42'
pattern='user=([[:alnum:]_]+)[[:space:]]+id=([0-9]+)'

if [[ $line =~ $pattern ]]; then
    echo "whole: ${BASH_REMATCH[0]}"    # user=alice id=42
    echo "user: ${BASH_REMATCH[1]}"     # alice
    echo "id: ${BASH_REMATCH[2]}"       # 42
fi
```

`${BASH_REMATCH[0]}` は全体、`[1]` 以降は括弧の順番に対応する。次の正規表現判定で値が変わるので、必要ならすぐ保存する。

### 正規表現は変数で持つと扱いやすい

```bash
line='hello world'
pattern='^hello[[:space:]]+world$'

if [[ $line =~ $pattern ]]; then
    echo 'match'
fi
```

**重要：`[[ $line =~ "$pattern" ]]` は、変数内の正規表現メタ文字をリテラルとして扱う。** 変数の正規表現を評価するなら `=~ $pattern`。

### リテラルのドット

```bash
name='file.txt'
pattern='\.txt$'
[[ $name =~ $pattern ]] && echo 'txt file'
```

### 大小文字の区別をしない

```bash
shopt -s nocasematch
[[ 'Error' =~ ^error$ ]] && echo 'match'
shopt -u nocasematch
```

`nocasematch` は他の Bash のパターン判定にも影響する点に注意。

---
## 13. Regex vs Glob

**正規表現（regex）**と**シェルのワイルドカード（glob）**は異なる。

| 目的 | glob | ERE |
|---|---|---|
| 任意の文字列 | `*` | `.*` |
| 任意の 1 文字 | `?` | `.` |
| `.txt` で終わる | `*.txt` | `\.txt$` |
| 数字が 1 文字以上 | 単純な glob では表現しにくい | `[0-9]+` |
| cat または dog | Bash の拡張 glob は別機構 | <code>(cat&#124;dog)</code> |

```bash
# glob：シェルのファイル名展開
for file in *.log; do
    echo "$file"
done

# glob：[[ == ]] の右辺
name='app.log'
[[ $name == *.log ]] && echo 'log file'

# regex：[[ =~ ]] の右辺
[[ $name =~ \.log$ ]] && echo 'log file'
```

`case`、`[[ == ]]`、`find -name`、`--include='*.py'` などは、基本的に **glob**。

---

## 14. Practical Patterns

以下は、断りがなければ **ERE**。`grep -E '...'` などで使用する。

### 数字・英字

```regex
[0-9]                      # 数字 1 桁
[0-9]+                     # 数字 1 桁以上
^[0-9]+$                   # 数字だけの行
^-?[0-9]+$                 # 符号なし、または - の付いた整数
^[+-]?[0-9]+$              # + / - も許容する整数
^[+-]?[0-9]+(\.[0-9]+)?$   # 整数または小数（12, -12.5 など）
^[A-Za-z]+$                # ASCII 英字だけ
^[A-Za-z0-9_]+$            # ASCII 英数字とアンダースコア
^[[:xdigit:]]+$            # 16 進数字だけ
```

小数の例は `.5`、`1.`、`1e3` のような表記は許可しない簡易版。

### 空白・コメント

```regex
^$                         # 空行
^[[:space:]]*$             # 空行・空白だけの行
^[[:space:]]+              # 行頭の空白
[[:space:]]+$              # 行末の空白
[[:space:]]{2,}            # 2 文字以上の連続空白
^[[:space:]]*#             # 先頭が # のコメント行（空白を許容）
^[[:space:]]*($|#)         # 空行・空白行・コメント行
```

### ファイル名・パス

```regex
\.txt$                     # .txt で終わる
\.(log|txt|csv)$           # .log / .txt / .csv で終わる
^/                         # / から始まる
^[^.].*                    # ドット以外で始まる
```

### 日付・時刻（形式だけ）

```regex
^[0-9]{4}-[0-9]{2}-[0-9]{2}$     # YYYY-MM-DD
^[0-9]{2}:[0-9]{2}$              # HH:MM
^[0-9]{2}:[0-9]{2}:[0-9]{2}$     # HH:MM:SS
```

`2026-99-99` や `99:99` も一致する。**実在する日付・時刻か**は別途検証する。

### IPv4 の見た目（厳密な IP 検証ではない）

```regex
^([0-9]{1,3}\.){3}[0-9]{1,3}$
```

`999.999.999.999` も一致する。厳密な検証には `ipaddress` などのパーサーを使う。

### メールアドレス（非常に簡易）

```regex
^[^@[:space:]]+@[^@[:space:]]+\.[^@[:space:]]+$
```

メールアドレスの仕様は複雑。これは**ざっくりした形式確認**にしか使えない。

### ログ・設定ファイル

```bash
# 重大なログ行を検索（大小文字無視）
grep -Ei 'error|warn|fatal' app.log

# IPv4 に見える文字列を抽出（範囲未検証）
grep -oE '([0-9]{1,3}\.){3}[0-9]{1,3}' access.log

# ERROR で始まる行
grep -E '^ERROR' app.log

# 空行・コメント行を除外
grep -Ev '^[[:space:]]*($|#)' config.txt

# 400〜599 の数字を含む行（HTTP ステータス欄とは限らない）
grep -E '(^|[^0-9])[45][0-9]{2}([^0-9]|$)' access.log
```

最後の例は**数字の形を探す**だけ。ログの決まった列の値を調べるなら `awk` などで列を特定する。

### 区切り文字のあるデータ

```bash
# 行末の数字を抽出
printf '%s\n' 'id=123' | grep -oE '[0-9]+$'
# 123

# user= の後にある値を取り出す
printf '%s\n' 'user=alice' | sed -nE 's/^user=([[:alnum:]_]+)$/\1/p'
# alice

# : より前の文字列
printf '%s\n' 'key:value:other' | grep -oE '^[^:]+'
# key

# 単純なカンマ区切り（引用符や改行を含まないケース）
printf '%s\n' 'alice,admin,30' | cut -d, -f1
# alice
```

本格的な CSV の解析（引用符・カンマ・改行を含む値）は、正規表現ではなく CSV パーサーを使う。

---

## 15. PCRE Extensions

以下は **POSIX ERE とは別の構文**。GNU grep で `-P` が利用可能な環境に限って使う。

```bash
grep --version
printf '%s\n' 'a1' | grep -P '\d'
```

| 記法（PCRE） | 意味 | ERE などでの代替 |
|---|---|---|
| `\d` | 数字 | `[0-9]` / `[[:digit:]]` |
| `\w` | 単語文字 | `[A-Za-z0-9_]`（ASCII 前提） |
| `\s` | 空白 | `[[:space:]]` |
| `\b` | 単語境界 | `grep -w`（完全な同等物ではない） |
| `(?:abc)` | キャプチャしないグループ | `(abc)`（キャプチャあり） |
| `*?` / `+?` / `??` | 最短の繰り返し | 否定文字クラスなど |
| `(?=abc)` | 肯定先読み | 検索を組み合わせる |
| `(?!abc)` | 否定先読み | `grep -v` など |
| `(?<=abc)` | 肯定後読み | `sed` キャプチャ置換など |

### 最短一致（非貪欲）

```bash
printf '%s\n' '<a><b>' | grep -oP '<.*?>'
# <a>
# <b>
```

この例なら ERE でも書ける。

```bash
printf '%s\n' '<a><b>' | grep -oE '<[^>]*>'
# <a>
# <b>
```

### 先読み・後読み

```bash
# user= の直後の値を抽出（固定長の後読み）
printf '%s\n' 'user=alice' | grep -oP '(?<=user=)[a-z]+'
# alice

# error の直後に _ignored が続かないものだけ
printf '%s\n' 'error error_ignored' | grep -oP 'error(?!_ignored)'
# error
```

`grep -P` は標準の grep オプションではなく、**利用可否は環境による**。必要がなければ ERE で書く。

---

## 16. Shell Quoting

### シェルでは基本的にシングルクォート

```bash
# 正規表現の $ や * をシェルに展開させない
grep -E '^[0-9]+$' numbers.txt

# 変数を使う場合はダブルクォート
pattern='^[0-9]+$'
grep -E -- "$pattern" numbers.txt
```

### Bash の `[[ =~ ]]` だけは注意

```bash
value='abc123'
pattern='^[a-z]+[0-9]+$'

[[ $value =~ $pattern ]]      # OK：正規表現として評価
[[ $value =~ "$pattern" ]]    # NG：特殊文字を文字どおり扱う
```

### 正規表現ではなく固定文字列がほしい場合

```bash
needle='a+b(c).txt'
grep -F -- "$needle" file.txt
```

ユーザー入力を**そのままの文字列**として検索するなら、エスケープの手間を避けられる `grep -F` が適切。

### `-` で始まる検索語

```bash
grep -F -- '-error' file.txt
grep -e '-error' file.txt
```

---

## 17. find / ripgrep

### `find -name` は glob

```bash
find . -type f -name '*.log'
find . -type f -iname '*.TXT'   # 大小文字を区別しない
```

### GNU `find -regex`

```bash
find . -regextype posix-extended -regex '.*\.(log|txt)$'
```

GNU `find -regex` は**パス全体**が一致対象。`-regextype` は GNU 拡張であり、macOS/BSD の `find` と仕様が違うことがある。

### ripgrep（`rg`）が入っている場合

```bash
rg 'TODO|FIXME' .
rg -n '^ERROR' ./logs
rg -g '*.py' 'def main' ./src
```

`rg` の既定の正規表現エンジンは POSIX ERE とは異なり、構文や使える機能に差がある。PCRE2 対応環境では `rg -P` が使用できる。

---

## 18. Exit Status

### grep の終了コード（GNU grep）

| コード | 意味 |
|---|---|
| `0` | 一致があった |
| `1` | 一致がなかった |
| `2` | エラー |

```bash
if grep -qE '^ERROR' app.log; then
    echo 'Error found'
else
    echo 'No match or grep failed'
fi
```

一致なしとエラーを区別したいときは終了コードを確認する。`set -e` が有効な場合には失敗するコマンドを条件式内で実行する。

```bash
if grep -qE '^ERROR' app.log; then
    echo 'Found'
else
    status=$?
    if (( status == 1 )); then
        echo 'Not found'
    else
        echo 'grep error' >&2
    fi
fi
```

---

## 19. Testing

### ファイルを作らずにテスト

```bash
printf '%s\n' 'abc' 'abc123' '123' | grep -E '^[a-z]+[0-9]+$'
# abc123
```

### 一致箇所だけ可視化

```bash
printf '%s\n' 'user=alice id=123' | grep -oE 'id=[0-9]+'
# id=123
```

### 行番号を付ける

```bash
grep -nE 'ERROR|WARN' app.log
```

### 一致してはいけない例も確認

```bash
printf '%s\n' '1234' '12a4' '12345' '' | grep -E '^[0-9]{4}$'
# 1234
```

正規表現を実データに使う前に、**一致する例・しない例の両方**をチェックする。

---
## 20. Common Pitfalls

### ドット `.` のエスケープ忘れ

```regex
file.txt      # fileXtxt にも一致しうる
file\.txt     # file.txt に一致
```

### `*` と `+` の混同

```regex
[0-9]*        # 空文字にも一致
[0-9]+        # 数字が 1 文字以上必要
```

### 部分一致と全体一致の混同

```regex
[0-9]+        # abc123def の中の 123 にも一致
^[0-9]+$      # 行全体が数字のときだけ一致
```

### `|` の優先順位

```regex
^yes|no$      # yes で始まる OR no で終わる
^(yes|no)$    # 行全体が yes または no
```

### ERE の `+` を BRE に持ち込む

```bash
grep -E 'a+' file.txt  # 正規表現として 1 回以上
grep 'a+' file.txt     # 標準 BRE では + は文字そのもの
```

### `\d` / `\s` / `\w` をどこでも使えると思う

```bash
# POSIX ERE を使うならこちら
grep -E '[[:digit:]]+' file.txt
grep -E '[[:space:]]+' file.txt
```

GNU grep には ERE に独自の拡張があるが、他の実装でも動くとは限らない。

### ERE で非貪欲 `.*?` を書く

```bash
grep -oE '<[^>]*>' file.txt   # ERE
grep -oP '<.*?>' file.txt     # PCRE が使える場合
```

### `sed` の置換で `\1` と `&` を混同する

```bash
printf '%s\n' 'x=12' | sed -E 's/([0-9]+)/[\1]/'
# x=[12]

printf '%s\n' 'x=12' | sed -E 's/[0-9]+/[&]/'
# x=[12]
```

### Bash の RHS をクォートする

```bash
pattern='^[0-9]+$'
value='123'
[[ $value =~ $pattern ]]    # パターンとして評価
[[ $value =~ "$pattern" ]]  # 正規表現の特殊文字がリテラル化
```

### grep と find の違いを見落とす

```bash
grep -E '\.log$' filenames.txt  # regex
find . -name '*.log'          # glob
```

### 形式確認を厳密な検証と勘違いする

`2026-99-99` や `999.999.999.999` は簡易パターンに一致しうる。**形式の一致と、実際に有効な値であることは別**。

### `grep -q` の不一致とエラーを混同する

ファイルがない場合や権限のない場合には、単なる「マッチなし」ではない。必要に応じて **終了コード 1 と 2** を区別する。

### 複数行を普通の grep で検索しようとする

通常の `grep` は**各行を別々に検索**する。行をまたぐパターンは、複数行対応のツールや Python などで処理する。

---

## 21. Quick Reference

| やりたいこと | 書き方 |
|---|---|
| 文字列を含む行 | `grep 'text' file.txt` |
| 大文字・小文字を無視 | `grep -i 'error' app.log` |
| OR 検索 | <code>grep -E 'error&#124;warn' app.log</code> |
| 行全体が OK | `grep -x 'OK' file.txt` |
| ERROR で始まる | `grep -E '^ERROR' app.log` |
| .log で終わる | `grep -E '\.log$' files.txt` |
| 数字を含む | `grep -E '[0-9]' file.txt` |
| 数字だけの行 | `grep -E '^[0-9]+$' file.txt` |
| 4 桁の数字 | `grep -E '^[0-9]{4}$' file.txt` |
| 完全な空行 | `grep -E '^$' file.txt` |
| 空白だけの行を含む | `grep -E '^[[:space:]]*$' file.txt` |
| マッチしない行 | `grep -v 'DEBUG' app.log` |
| 一致箇所だけ | `grep -oE '[0-9]+' file.txt` |
| 行番号付き | `grep -n 'TODO' file.txt` |
| 前後 2 行を表示 | `grep -C 2 'ERROR' app.log` |
| 文字どおりに探す | `grep -F 'a.b' file.txt` |
| すべて置換 | `sed -E 's/foo/bar/g' file.txt` |
| 連続空白をまとめる | `sed -E 's/[[:space:]]+/ /g' file.txt` |
| キャプチャして置換 | `sed -E 's/([0-9]+)/[\1]/g'` |
| 1 列目を表示 | `awk '{print $1}' file.txt` |
| `:` 区切りの 1 列目 | `awk -F: '{print $1}' file.txt` |
| Bash で判定 | `[[ $value =~ ^[0-9]+$ ]]` |
| Bash でキャプチャ | `${BASH_REMATCH[1]}` |
| glob でファイル名検索 | `find . -name '*.log'` |
| PCRE の最短一致 | `grep -oP '<.*?>' file.txt` |

**迷ったら：検索は `grep -E`、置換は `sed -E`、列処理は `awk`、Bash の条件は `[[ =~ ]]`。**

---

## 22. References

- [GNU grep Manual](https://www.gnu.org/software/grep/manual/grep.html)
- [GNU sed Manual](https://www.gnu.org/software/sed/manual/sed.html)
- [GNU Bash Manual — Conditional Constructs](https://www.gnu.org/software/bash/manual/html_node/Conditional-Constructs.html)
- [GNU Awk Manual](https://www.gnu.org/software/gawk/manual/gawk.html)
- [GNU findutils Manual](https://www.gnu.org/software/findutils/manual/html_mono/find.html)

主な想定環境は **Linux の GNU 系ツール + Bash**。macOS/BSD、BusyBox、他の言語の正規表現ではオプションや構文の一部が異なる。
