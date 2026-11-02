# Python Cheat Sheet

> **Python 3.10+ / 基本文法・標準ライブラリ編**  
> 「何を書けばよいか忘れたとき」に、そのまま使える短いコード例から探すためのチートシート。  
> 外部パッケージの専門的な使い方や、高度なメタプログラミングは扱わない。

**読み方**

- コードブロックは基本的に Python 3 の構文。`bash` と書かれたブロックだけシェルで実行する。
- サンプルの変数やファイル名は適宜置き換える。各コードブロックは、原則として**独立した例**。
- インデックスは **0 始まり**、範囲の終端は原則 **含まない**。
- `#` はコメント、`>>>` は対話モードの入力例に使われることがある。

## Contents

1. [Run Python（実行・環境）](#1-run-python)
2. [Syntax Basics（文法の基本）](#2-syntax-basics)
3. [Variables & Types（変数・型）](#3-variables--types)
4. [Input & Output（入出力）](#4-input--output)
5. [Operators（演算子）](#5-operators)
6. [Strings（文字列）](#6-strings)
7. [Lists（リスト）](#7-lists)
8. [Tuples（タプル）](#8-tuples)
9. [Dictionaries（辞書）](#9-dictionaries)
10. [Sets（集合）](#10-sets)
11. [Indexing & Unpacking（添字・展開）](#11-indexing--unpacking)
12. [Conditionals（条件分岐）](#12-conditionals)
13. [Loops（繰り返し）](#13-loops)
14. [Comprehensions（内包表記）](#14-comprehensions)
15. [Functions（関数）](#15-functions)
16. [Scope & Lambda（スコープ・無名関数）](#16-scope--lambda)
17. [Exceptions（例外処理）](#17-exceptions)
18. [Classes（クラス）](#18-classes)
19. [Modules & Imports（モジュール）](#19-modules--imports)
20. [Built-in Functions（組み込み関数）](#20-built-in-functions)
21. [File I/O（ファイル入出力）](#21-file-io)
22. [Paths & Directories（パス・ディレクトリ）](#22-paths--directories)
23. [JSON & CSV（データ形式）](#23-json--csv)
24. [Date & Time（日付・時刻）](#24-date--time)
25. [Regular Expressions（正規表現）](#25-regular-expressions)
26. [Command-line Arguments（CLI 引数）](#26-command-line-arguments)
27. [Environment & Subprocess（環境変数・外部コマンド）](#27-environment--subprocess)
28. [Type Hints（型ヒント）](#28-type-hints)
29. [Iterators & Generators（イテレータ・ジェネレータ）](#29-iterators--generators)
30. [Useful Standard Library（よく使う標準ライブラリ）](#30-useful-standard-library)
31. [Common Pitfalls（間違えやすい点）](#31-common-pitfalls)
32. [Small Script Template（実用スクリプトの型）](#32-small-script-template)
33. [Quick Reference（逆引き）](#33-quick-reference)

---

## 1. Run Python

### 実行

```bash
python3 --version
python3 script.py             # ファイルを実行
python3 -i script.py          # 実行後に対話モードへ
python3 -c 'print(1 + 2)'    # 1 行実行
python3 -m module_name       # モジュールとして実行
python3                       # 対話モード（終了は exit()）
```

### Shebang / スクリプトの入口

```python
#!/usr/bin/env python3


def main():
    print("Hello, Python!")


if __name__ == "__main__":
    main()
```

```bash
chmod +x script.py
./script.py
```

`if __name__ == "__main__":` は、ファイルを**直接実行したときだけ** `main()` を呼ぶための定番。

### 仮想環境（必要な場合）

```bash
python3 -m venv .venv
source .venv/bin/activate       # Linux / macOS
# Windows PowerShell: .venv\Scripts\Activate.ps1
python3 -m pip --version
# 必要なパッケージがある場合のみ: python3 -m pip install パッケージ名
deactivate
```

---

## 2. Syntax Basics

### インデントでブロックを表す

```python
if True:
    print("条件が真")
    print("同じブロック")

print("ブロックの外")
```

- 通常は **スペース 4 個**でインデントする。
- `if`、`for`、`def`、`class` などの行末には `:` を付ける。
- `{}` ではなくインデントが文のまとまりを決める。

### コメント・複数行・何もしない文

```python
# 1 行コメント

# 丸括弧などの中では改行できる
result = (
    10 + 20
    + 30
)

if result > 0:
    pass  # 後から実装する場所
```

### 複数行文字列 / docstring

```python
message = """1 行目
2 行目"""


def greet(name):
    """名前を受け取り、挨拶文を返す。"""
    return f"Hello, {name}"
```

---

## 3. Variables & Types

### 代入

```python
name = "Alice"       # str: 文字列
age = 20             # int: 整数
height = 1.65        # float: 小数
active = True        # bool: 真偽値
value = None         # 値がない

x, y = 10, 20        # 同時代入
x, y = y, x          # 値の交換
count = 0
count += 1           # count = count + 1
```

Python の変数には型を宣言する必要がない。型は**値**に付いている。

### 型の確認・変換

```python
print(type(42))                  # <class 'int'>
print(isinstance(42, int))       # True

int("123")                       # 123
float("3.14")                    # 3.14
str(123)                        # "123"
bool(0)                         # False
bool("hello")                   # True
list("abc")                     # ['a', 'b', 'c']
```

### 定数（慣習）

```python
MAX_RETRIES = 3
DEFAULT_TIMEOUT = 5.0
```

Python には通常の変数代入を禁止する定数構文はない。**大文字**は「変更しない」という慣習。

### `None` と真偽値

```python
value = None
if value is None:               # None 判定は is / is not
    print("値なし")

# 偽として評価される代表例
# False, None, 0, 0.0, "", [], {}, set(), ()
items = []
if not items:
    print("空")
```

---

## 4. Input & Output

### 表示

```python
print("Hello")
print("A", "B", "C")             # A B C
print("A", "B", sep=",")        # A,B
print("進捗", end="...")           # 改行しない
print("完了")

name = "Alice"
print(f"Hello, {name}!")        # f-string
print(f"{3.14159:.2f}")         # 3.14
print(f"{10000:,}")             # 10,000
```

### 標準入力

```python
name = input("名前: ")           # 戻り値は必ず str
age = int(input("年齢: "))      # 数値が必要なら変換
print(name, age)
```

不正な数値入力は `ValueError` になる。必要なら `try / except` で処理する。

### 標準エラー出力

```python
import sys

print("エラーが発生", file=sys.stderr)
```

---

## 5. Operators

### 算術演算子

| 演算子 | 意味 | 例 | 結果 |
|---|---|---|---|
| `+` | 加算 | `7 + 3` | `10` |
| `-` | 減算 | `7 - 3` | `4` |
| `*` | 乗算 | `7 * 3` | `21` |
| `/` | 除算（小数） | `7 / 3` | `2.333...` |
| `//` | 切り捨て除算 | `7 // 3` | `2` |
| `%` | 剰余 | `7 % 3` | `1` |
| `**` | べき乗 | `2 ** 3` | `8` |

```python
x = 10
x += 2       # 12
x -= 1       # 11
x *= 3       # 33
x /= 2       # 16.5（float になる）
```

`//` は**負の無限大方向**への切り捨て（例: `-7 // 3 == -3`）。

### 比較演算子

```python
x = 10
x == 10      # 等しい
x != 5       # 等しくない
x > 5
x >= 10
x < 20
x <= 10
1 <= x < 100  # 比較をつなげられる
```

### 論理演算子

```python
age = 20
active = True

if age >= 18 and active:
    print("利用可能")

if age < 18 or not active:
    print("制限あり")
```

`and` は両方が真、`or` はどちらかが真、`not` は否定。`and` / `or` は必要な側だけ評価する（短絡評価）。

### 含まれるか / 同じオブジェクトか

```python
"py" in "python"               # True
3 in [1, 2, 3]                 # True
"id" in {"id": 1}              # True（辞書ではキーを調べる）
4 not in [1, 2, 3]             # True

# == は値の比較、is は同一オブジェクトかの比較
[1, 2] == [1, 2]               # True
```

### ビット演算（必要な場合）

```python
5 & 3        # AND: 1
5 | 3        # OR: 7
5 ^ 3        # XOR: 6
~5           # ビット反転: -6
5 << 1       # 左シフト: 10
5 >> 1       # 右シフト: 2
```

---

## 6. Strings

### 文字列の作成

```python
s1 = 'single quote'
s2 = "double quote"
s3 = "line1\nline2"          # 改行
s4 = "tab\tseparated"        # タブ
s5 = r"C:\new\test"         # raw 文字列（バックスラッシュを原則そのまま扱う）
s6 = """複数行
のテキスト"""
```

### 結合・繰り返し・長さ

```python
"Hello" + " " + "World"    # 'Hello World'
"ha" * 3                    # 'hahaha'
len("Python")               # 6
"-".join(["a", "b", "c"])  # 'a-b-c'
```

### 文字列の添字・スライス

```python
s = "Python"
s[0]             # 'P'
s[-1]            # 'n'
s[1:4]           # 'yth'（4 は含まない）
s[:3]            # 'Pyt'
s[3:]            # 'hon'
s[::2]           # 'Pto'
s[::-1]          # 'nohtyP'
```

文字列は**変更不可（immutable）**。`s[0] = "X"` はできない。

### よく使う文字列メソッド

```python
s = "  Hello Python  "
s.strip()                    # 両端の空白・改行を除去
s.lstrip()                   # 左だけ
s.rstrip()                   # 右だけ
s.lower()                    # 小文字へ
s.upper()                    # 大文字へ
s.replace("Python", "World")  # 置換
s.find("Python")             # 最初の位置（なければ -1）
s.count("l")                 # 出現回数
s.startswith("  He")         # 接頭辞の判定
s.endswith("  ")             # 接尾辞の判定

"a,b,c".split(",")           # ['a', 'b', 'c']
" a  b   c ".split()         # ['a', 'b', 'c']（連続空白をまとめる）
"a\nb\n".splitlines()         # ['a', 'b']
"abc123".isalnum()           # 英数字か
"123".isdigit()             # 数字か
"abc".isalpha()             # 文字か
```

### f-string / 書式指定

```python
name = "Alice"
score = 92.345
print(f"{name}: {score:.1f}")   # Alice: 92.3
print(f"{7:03d}")             # 007
print(f"{0.125:.1%}")          # 12.5%
print(f"{255:02x}")            # ff（16 進数）
print(f"{name!r}")             # 'Alice'（repr 形式）
```

### バイト列との変換

```python
text = "こんにちは"
data = text.encode("utf-8")    # str → bytes
restored = data.decode("utf-8") # bytes → str
```

---

## 7. Lists

リストは**順序あり・変更可能**。複数の値をまとめて扱う。

### 作成・取得・変更

```python
items = ["apple", "banana", "cherry"]
items[0]                      # 'apple'
items[-1]                     # 'cherry'
items[1] = "orange"           # 要素の変更
items[0:2]                    # 最初の 2 要素
len(items)                    # 要素数
"orange" in items             # True
```

### 追加・削除

```python
nums = [1, 2, 3]
nums.append(4)                 # 末尾に 1 個追加
nums.extend([5, 6])           # 複数追加
nums.insert(0, 0)             # 指定位置へ挿入
nums.remove(3)                # 値 3 を最初に見つけた位置から削除
last = nums.pop()             # 最後の要素を取り出して削除
first = nums.pop(0)           # 先頭を取り出す
nums.clear()                  # 全削除
```

`remove()` は値がなければ `ValueError`、`pop()` は対象がなければ `IndexError`。

### ソート・コピー

```python
nums = [3, 1, 2]
nums.sort()                    # 元のリストを変更（返り値は None）
nums.sort(reverse=True)       # 降順
ordered = sorted(nums)        # 新しいリストで返す
copy_nums = nums.copy()       # 浅いコピー

names = ["Bob", "alice", "Carol"]
names.sort(key=str.lower)     # 大小文字を無視して並べる
```

### 要素を調べる

```python
nums = [10, 20, 20, 30]
nums.index(20)                # 最初に見つかった位置: 1
nums.count(20)                # 2
sum(nums)                     # 80
min(nums)                     # 10
max(nums)                     # 30
```

---

## 8. Tuples

タプルは**順序あり・要素の差し替え不可**。固定的な組を返す場合などに使う。

```python
point = (10, 20)
point[0]                      # 10
x, y = point                  # アンパック

single = (42,)                # 1 要素タプルにはカンマが必要
empty = ()

# 要素の差し替えは不可: point[0] = 99
```

タプル自体は変更不可だが、**内部に含めたリストなどは変更可能**。

---

## 9. Dictionaries

辞書は**キー → 値**の対応表。キーは重複せず、文字列や数値などのハッシュ可能な値を使う。

### 作成・取得・変更

```python
user = {"name": "Alice", "age": 20}
user["name"]                  # 'Alice'
user["age"] = 21              # 更新
user["email"] = "a@example.com"  # 新しいキー

user.get("address")           # なければ None
user.get("address", "未登録") # なければ既定値
"age" in user                 # キーの存在確認
```

`user["missing"]` は `KeyError`。キーがない可能性があるときは `get()` を利用。

### 削除・走査

```python
scores = {"Alice": 90, "Bob": 80}
removed = scores.pop("Bob")   # 値を返して削除

for key in scores:
    print(key, scores[key])

for key, value in scores.items():
    print(key, value)

list(scores.keys())           # キー一覧
list(scores.values())         # 値一覧
```

### 追加・マージ

```python
config = {"host": "localhost", "port": 8000}
config.update({"port": 9000, "debug": True})
merged = config | {"timeout": 5}  # 新しい辞書を作る（3.9+）
```

辞書は**挿入順を保持**する（Python 3.7+）。

---

## 10. Sets

集合は**重複なし・順序保証なし**。重複排除や集合演算に利用。

```python
values = {1, 2, 2, 3}       # {1, 2, 3}
empty_set = set()            # {} は空の辞書

values.add(4)
values.discard(99)           # なければ何もしない
values.remove(1)            # なければ KeyError
2 in values                 # 高速な存在判定に便利

unique = list(set([1, 2, 2, 3]))  # 重複排除（元の順序は維持されない）
```

### 集合演算

```python
a = {1, 2, 3}
b = {3, 4, 5}

a | b         # 和集合: {1, 2, 3, 4, 5}
a & b         # 積集合: {3}
a - b         # 差集合: {1, 2}
a ^ b         # 対称差: {1, 2, 4, 5}
a <= b        # a は b の部分集合か
```

順序を維持して重複排除するなら `list(dict.fromkeys(items))` が便利。

---

## 11. Indexing & Unpacking

### スライスの共通ルール

```python
# sequence[start:stop:step]
nums = [0, 1, 2, 3, 4, 5]
nums[1:4]         # [1, 2, 3]
nums[:3]          # [0, 1, 2]
nums[3:]          # [3, 4, 5]
nums[::2]         # [0, 2, 4]
nums[::-1]        # [5, 4, 3, 2, 1, 0]
```

`str`、`list`、`tuple` などに使用。通常のインデックスは範囲外なら `IndexError`、スライスは範囲外でも切り詰められる。

### アンパック

```python
x, y = [10, 20]
first, *middle, last = [1, 2, 3, 4]
# first=1, middle=[2, 3], last=4

a = [1, 2]
b = [3, 4]
combined = [*a, *b]          # [1, 2, 3, 4]

left = {"a": 1}
right = {"b": 2}
both = {**left, **right}      # {'a': 1, 'b': 2}
```

---

## 12. Conditionals

### `if / elif / else`

```python
score = 75

if score >= 90:
    grade = "A"
elif score >= 70:
    grade = "B"
else:
    grade = "C"

print(grade)                  # B
```

### 条件式（短い if / else）

```python
age = 20
status = "adult" if age >= 18 else "minor"
```

### `match / case`（Python 3.10+）

```python
command = "start"

match command:
    case "start":
        print("開始")
    case "stop" | "quit":
        print("停止")
    case _:
        print("不明なコマンド")
```

単純な分岐は `if` で十分。多数の定型パターンを分岐させたいときに `match` を使う。

---

## 13. Loops

### `for` / `range`

```python
for name in ["Alice", "Bob"]:
    print(name)

for i in range(5):            # 0, 1, 2, 3, 4
    print(i)

for i in range(2, 10, 2):    # 2, 4, 6, 8
    print(i)
```

### `enumerate` / `zip`

```python
names = ["Alice", "Bob"]
scores = [90, 80]

for index, name in enumerate(names):
    print(index, name)         # 0 Alice / 1 Bob

for index, name in enumerate(names, start=1):
    print(index, name)         # 1 Alice / 2 Bob

for name, score in zip(names, scores):
    print(name, score)
```

`zip` は通常、**短い方の反復が終わると停止**する。

### `while`

```python
count = 0
while count < 3:
    print(count)
    count += 1                 # Python に ++ 演算子はない
```

### `break / continue`

```python
for i in range(10):
    if i == 3:
        continue               # この回だけ飛ばす
    if i == 7:
        break                  # ループを抜ける
    print(i)
```

### `for / else`（必要なら）

```python
numbers = [1, 3, 5]
for number in numbers:
    if number % 2 == 0:
        print("偶数が見つかった")
        break
else:
    print("偶数なし")           # break しなかった場合だけ実行
```

---

## 14. Comprehensions

繰り返し処理で**新しいコレクションを作る**短い書き方。

### リスト内包表記

```python
squares = [x * x for x in range(5)]
# [0, 1, 4, 9, 16]

evens = [x for x in range(10) if x % 2 == 0]
# [0, 2, 4, 6, 8]

labels = ["even" if x % 2 == 0 else "odd" for x in range(4)]
# ['even', 'odd', 'even', 'odd']
```

### 辞書・集合内包表記

```python
square_map = {x: x * x for x in range(3)}
# {0: 0, 1: 1, 2: 4}

unique_lengths = {len(word) for word in ["a", "bb", "cc"]}
# {1, 2}
```

### ジェネレータ式

```python
total = sum(x * x for x in range(100))
```

読みづらくなるほど内包表記を入れ子にするより、普通の `for` を使う。

---

## 15. Functions

### 定義・呼び出し・戻り値

```python
def add(a, b):
    return a + b

result = add(2, 3)            # 5
```

`return` を書かない関数は `None` を返す。

### デフォルト引数・キーワード引数

```python
def greet(name, message="Hello"):
    return f"{message}, {name}"

greet("Alice")
greet("Alice", "Hi")
greet(name="Bob", message="Welcome")
```

### 複数値を返す

```python
def min_max(values):
    return min(values), max(values)  # タプルを返す

small, large = min_max([3, 1, 5])
```

### 可変長引数

```python
def total(*numbers):        # 位置引数をタプルで受け取る
    return sum(numbers)

print(total(1, 2, 3))        # 6


def show_user(**fields):    # キーワード引数を辞書で受け取る
    print(fields)

show_user(name="Alice", age=20)
```

### 引数を展開して渡す

```python
def add(a, b):
    return a + b

args = [2, 3]
options = {"a": 5, "b": 8}
add(*args)                   # add(2, 3)
add(**options)               # add(a=5, b=8)
```

### キーワード専用引数

```python
def connect(host, *, timeout=5):
    print(host, timeout)

connect("localhost", timeout=10)
# connect("localhost", 10) は不可
```

### docstring

```python
def area(width, height):
    """長方形の面積を計算する。"""
    return width * height

help(area)                    # 関数の説明を表示
```

---

## 16. Scope & Lambda

### ローカル変数とグローバル変数

```python
x = 10                       # モジュールの変数


def show():
    x = 20                   # 関数内だけの別の変数
    print(x)

show()                       # 20
print(x)                     # 10
```

関数内で外側の変数を**再代入**する必要があるときに `global` / `nonlocal` が使えるが、まずは引数と `return` で値を受け渡す設計が分かりやすい。

```python
def increment(value):
    return value + 1

count = 0
count = increment(count)
```

### `lambda`（短い無名関数）

```python
square = lambda x: x * x
print(square(3))              # 9

users = [{"name": "Bob", "age": 30}, {"name": "Alice", "age": 20}]
by_age = sorted(users, key=lambda user: user["age"])
```

処理が長いなら `lambda` より `def` を使う。

---

## 17. Exceptions

### `try / except`

```python
text = "abc"

try:
    number = int(text)
except ValueError:
    print("整数に変換できません")
```

### 例外を変数で受け取る

```python
try:
    result = 10 / 0
except ZeroDivisionError as exc:
    print(f"計算失敗: {exc}")
```

### `else / finally`

```python
try:
    value = int("123")
except ValueError:
    print("変換失敗")
else:
    print("変換成功", value)     # 例外が起きなかった場合
finally:
    print("終了処理")           # 通常の完了・例外発生どちらでも実行
```

### `raise`（例外を発生させる）

```python
def divide(a, b):
    if b == 0:
        raise ValueError("b は 0 にできません")
    return a / b
```

よく使う例外: `ValueError`（値が不正）、`TypeError`（型・引数が不正）、`KeyError`、`IndexError`、`FileNotFoundError`、`PermissionError`、`OSError`。

**原則:** `except:` で何でも捕まえず、想定した例外を指定する。

---

## 18. Classes

### 基本的なクラス

```python
class User:
    def __init__(self, name, age):
        self.name = name      # インスタンス属性
        self.age = age

    def greet(self):
        return f"Hello, {self.name}"


user = User("Alice", 20)
print(user.name)              # Alice
print(user.greet())           # Hello, Alice
user.age = 21
```

- `__init__` はインスタンス初期化時に呼ばれる。
- `self` はそのインスタンスを指し、メソッド定義の第 1 引数に書く。
- `self.name` は各インスタンスが持つ属性。

### 継承・`super()`

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "..."


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        return "Woof!"


dog = Dog("Pochi")
print(dog.name, dog.speak())
print(isinstance(dog, Animal))  # True
```

### `@property`（属性としてアクセス）

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height


r = Rectangle(3, 4)
print(r.area)                  # 12（r.area() ではない）
```

---

## 19. Modules & Imports

### 標準ライブラリの読み込み

```python
import math
print(math.sqrt(16))          # 4.0

from pathlib import Path
path = Path("data.txt")

import datetime as dt
print(dt.date.today())
```

### 自作モジュールを利用

`utils.py`:

```python
def greet(name):
    return f"Hello, {name}"
```

同じディレクトリの `main.py`:

```python
import utils

print(utils.greet("Alice"))
```

### 直接実行時だけ処理

```python
def main():
    print("直接実行された")


if __name__ == "__main__":
    main()
```

複数ファイルに分けるとき、`import` しただけで処理が走らないようにする。

---

## 20. Built-in Functions

| 関数 | 用途 | 例 |
|---|---|---|
| `len(x)` | 長さ・要素数 | `len([1, 2])` → `2` |
| `sum(xs)` | 合計 | `sum([1, 2, 3])` → `6` |
| `min(xs)` / `max(xs)` | 最小・最大 | `max([1, 4])` → `4` |
| `abs(x)` | 絶対値 | `abs(-5)` → `5` |
| `round(x, n)` | 丸め | `round(3.14159, 2)` → `3.14` |
| `sorted(xs)` | ソートした新リスト | `sorted([3, 1])` → `[1, 3]` |
| `reversed(xs)` | 逆順イテレータ | `list(reversed([1, 2]))` |
| `enumerate(xs)` | 連番付き反復 | `for i, x in enumerate(xs):` |
| `zip(a, b)` | 複数列を並行反復 | `list(zip([1], [2]))` |
| `range(n)` | 連続整数を反復 | `range(5)` |
| `any(xs)` | 1 つでも真なら真 | `any([False, True])` |
| `all(xs)` | すべて真なら真 | `all([True, True])` |
| `isinstance(x, T)` | 型判定 | `isinstance(1, int)` |
| `type(x)` | 型を取得 | `type("abc")` |
| `int` / `float` / `str` | 型変換 | `int("42")` |
| `list` / `tuple` / `set` / `dict` | コレクション生成 | `set([1, 1, 2])` |
| `help(x)` | ヘルプ表示 | `help(str.split)` |
| `dir(x)` | 属性名の一覧 | `dir(str)` |
| `print(x)` | 表示 | `print("hi")` |
| `input()` | 文字列入力 | `input("name: ")` |

### 便利な組み合わせ

```python
nums = [1, 2, 3, 4]
any(n > 3 for n in nums)         # True
all(n > 0 for n in nums)         # True
sorted(nums, reverse=True)       # [4, 3, 2, 1]

records = [{"id": 2}, {"id": 1}]
sorted(records, key=lambda row: row["id"])
```

---

## 21. File I/O

基本は `with open(...)`。ブロックを抜けると**自動でファイルが閉じる**。

### 全文読み込み

```python
with open("data.txt", "r", encoding="utf-8") as f:
    text = f.read()
```

### 1 行ずつ読む

```python
with open("data.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.rstrip("\n"))
```

### 書き込み・追記

```python
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("Hello\n")        # 上書き。既存の内容は消える

with open("output.txt", "a", encoding="utf-8") as f:
    f.write("追加行\n")        # 追記
```

### 開くモード

| モード | 意味 |
|---|---|
| `"r"` | 読み込み（ファイルがなければエラー） |
| `"w"` | 書き込み（既存内容を消す） |
| `"a"` | 追記 |
| `"x"` | 新規作成（既存ならエラー） |
| `"b"` | バイナリ（`"rb"`、`"wb"` など） |
| `"+"` | 読み書き両方（`"r+"` など） |

### バイナリファイル

```python
with open("image.bin", "rb") as f:
    data = f.read()            # bytes

with open("copy.bin", "wb") as f:
    f.write(data)
```

### ファイルがない場合

```python
try:
    with open("config.txt", encoding="utf-8") as f:
        config = f.read()
except FileNotFoundError:
    config = ""
```

---

## 22. Paths & Directories

ファイル操作には `pathlib.Path` が便利。`os.path` より読みやすいことが多い。

### パスの組み立て・判定

```python
from pathlib import Path

path = Path("logs") / "app.log"
path.name                     # 'app.log'
path.stem                     # 'app'
path.suffix                   # '.log'
path.parent                   # Path('logs')
path.exists()                 # 存在するか
path.is_file()                # ファイルか
path.is_dir()                 # ディレクトリか
```

### 読み書き・ディレクトリ生成

```python
from pathlib import Path

folder = Path("output")
folder.mkdir(parents=True, exist_ok=True)

file = folder / "result.txt"
file.write_text("Hello\n", encoding="utf-8")
text = file.read_text(encoding="utf-8")
```

### ファイル一覧

```python
from pathlib import Path

for path in Path(".").iterdir():
    print(path)

for path in Path(".").glob("*.py"):
    print(path)

for path in Path(".").rglob("*.log"):
    print(path)                # サブディレクトリも再帰検索
```

### その他の操作

```python
from pathlib import Path
import shutil

source = Path("source.txt")

# 存在するファイルを操作する場合の例
# source.rename("renamed.txt")           # 移動・改名
# source.unlink()                        # ファイル削除
# shutil.copy2("source.txt", "copy.txt")  # ファイルコピー
# shutil.rmtree("temp_dir")              # ディレクトリごと削除（要注意）
```

現在位置とスクリプト位置は異なる場合がある。

```python
from pathlib import Path

cwd = Path.cwd()                         # 実行時の作業ディレクトリ
script_dir = Path(__file__).resolve().parent  # スクリプトがある場所
```

`__file__` は通常のスクリプト内で使う。対話モード等では定義されない場合がある。

---

## 23. JSON & CSV

### JSON: 文字列と Python の値を相互変換

```python
import json

user = {"name": "Alice", "active": True, "age": 20}
text = json.dumps(user, ensure_ascii=False, indent=2)  # dict → JSON文字列
restored = json.loads(text)                           # JSON文字列 → dict
```

JSON の `true` / `false` / `null` は、Python では `True` / `False` / `None`。

### JSON: ファイルへの保存・読み込み

```python
import json

with open("data.json", "w", encoding="utf-8") as f:
    json.dump({"name": "Alice"}, f, ensure_ascii=False, indent=2)

with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)
```

### CSV: 行単位

```python
import csv

with open("data.csv", "r", encoding="utf-8", newline="") as f:
    for row in csv.reader(f):
        print(row)                       # リストとして取得

with open("out.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "age"])
    writer.writerow(["Alice", 20])
```

### CSV: ヘッダー付き辞書形式

```python
import csv

with open("data.csv", "r", encoding="utf-8", newline="") as f:
    for row in csv.DictReader(f):
        print(row["name"])              # ヘッダー名で参照

with open("out.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "age"])
    writer.writeheader()
    writer.writerow({"name": "Bob", "age": 25})
```

CSV から読み込んだ各セルは基本的に**文字列**。必要に応じて `int()` / `float()` で変換する。

---

## 24. Date & Time

```python
from datetime import date, datetime, timedelta, timezone

today = date.today()                 # 今日の日付（ローカル）
now = datetime.now().astimezone()    # 現在の日時（ローカルのタイムゾーン付き）
now_utc = datetime.now(timezone.utc) # UTC

tomorrow = today + timedelta(days=1)
last_hour = now - timedelta(hours=1)
```

### 文字列との相互変換

```python
from datetime import datetime

now = datetime.now()
text = now.strftime("%Y-%m-%d %H:%M:%S")
parsed = datetime.strptime("2026-11-02", "%Y-%m-%d")
```

主な指定子: `%Y` 年、`%m` 月、`%d` 日、`%H` 時（24時間）、`%M` 分、`%S` 秒。

### 経過時間の測定

```python
import time

start = time.perf_counter()
# ここに測定したい処理を書く
elapsed = time.perf_counter() - start
print(f"{elapsed:.3f} 秒")

time.sleep(1)                  # 1 秒停止
```

---

## 25. Regular Expressions

正規表現は `re` を使う。パターンは `r"..."`（raw 文字列）で書くと扱いやすい。

### 検索・一致判定

```python
import re

text = "ID: 123, ID: 456"
match = re.search(r"\d+", text)   # 最初に見つかった部分
if match:
    print(match.group())          # '123'

re.findall(r"\d+", text)         # ['123', '456']
re.fullmatch(r"\d+", "12345")    # 全体が一致すれば Match オブジェクト
```

### 置換・分割・グループ

```python
import re

re.sub(r"\s+", " ", "a   b\tc")       # 'a b c'
re.split(r"[,;]\s*", "a,b; c")        # ['a', 'b', 'c']

m = re.search(r"(\w+)@(\w+\.\w+)", "user@example.com")
if m:
    print(m.group(1))               # user
    print(m.group(2))               # example.com
```

### 頻出パターン

| パターン | 意味 |
|---|---|
| `.` | 任意の 1 文字（通常は改行を除く） |
| `\d` / `\D` | 数字 / 数字以外 |
| `\w` / `\W` | 単語文字 / その以外 |
| `\s` / `\S` | 空白文字 / 空白以外 |
| `^` / `$` | 文字列（または行）の先頭 / 末尾 |
| `*` / `+` / `?` | 0 回以上 / 1 回以上 / 0 または 1 回 |
| `{n}` / `{n,m}` | n 回 / n〜m 回 |
| `[abc]` | a、b、c のどれか |
| `[^abc]` | a、b、c 以外 |
| `(abc)` | グループ化・キャプチャ |
| `a\|b` | a または b（表では `\|` と表記） |

---

## 26. Command-line Arguments

### `sys.argv`（簡単な引数取得）

`python3 script.py Alice` のように実行する場合:

```python
import sys

print(sys.argv[0])                # スクリプト名
if len(sys.argv) >= 2:
    print(sys.argv[1])            # 'Alice'
else:
    print("引数なし")
```

### `argparse`（おすすめ）

```python
import argparse

parser = argparse.ArgumentParser(description="挨拶するスクリプト")
parser.add_argument("name", help="相手の名前")
parser.add_argument("-n", "--count", type=int, default=1, help="繰り返し回数")
parser.add_argument("--quiet", action="store_true", help="出力を抑制")
args = parser.parse_args()

if not args.quiet:
    for _ in range(args.count):
        print(f"Hello, {args.name}")
```

```bash
python3 script.py Alice
python3 script.py Alice --count 3
python3 script.py Alice -n 3 --quiet
python3 script.py --help           # 自動で使い方を表示
```

### 終了コード

```python
import sys

# 正常終了 = 0、異常終了 = 通常 0 以外
sys.exit(0)
# sys.exit(1)
```

---

## 27. Environment & Subprocess

### 環境変数

```python
import os

home = os.environ.get("HOME")              # 未設定なら None
mode = os.getenv("APP_MODE", "development") # デフォルト値
# 必須の場合は os.environ["APP_MODE"]（未設定なら KeyError）
```

### 外部コマンド実行

```python
import subprocess

result = subprocess.run(
    ["echo", "hello"],
    check=True,              # 0 以外の終了コードなら例外
    capture_output=True,     # stdout / stderr を取得
    text=True,               # bytes ではなく str で取得
    timeout=10,
)
print(result.stdout.strip())
print(result.returncode)
```

外部コマンドへの引数は**文字列のリスト**で渡すのが基本。ユーザー入力を連結して安易に `shell=True` に渡すと、コマンド注入の危険がある。

---

## 28. Type Hints

型ヒントは読みやすさや静的解析を助けるための注記。**通常、実行時に自動で型を強制しない**。

```python
name: str = "Alice"
count: int = 3
scores: list[int] = [80, 90]
user: dict[str, int] = {"age": 20}
optional_name: str | None = None     # Python 3.10+


def average(values: list[float]) -> float:
    return sum(values) / len(values)


def notify(message: str) -> None:
    print(message)
```

空リストで `average([])` を呼べば `ZeroDivisionError` になる。型ヒントだけで事前条件は保証されない。

---

## 29. Iterators & Generators

### イテラブルとイテレータ

```python
items = [10, 20, 30]         # 反復可能（iterable）
it = iter(items)             # イテレータを取得
next(it)                     # 10
next(it)                     # 20
```

### `yield`（値を 1 個ずつ返す）

```python
def count_up(limit):
    for i in range(limit):
        yield i

for n in count_up(3):
    print(n)                  # 0, 1, 2
```

一度にすべての結果をリストにせず、**必要なときに次の値を生成**できる。通常の処理は `for` とリストだけでも十分書ける。

---

## 30. Useful Standard Library

### `collections.Counter`（出現回数）

```python
from collections import Counter

counts = Counter(["a", "b", "a"])
print(counts["a"])           # 2
print(counts.most_common(1)) # [('a', 2)]
```

### `random`（乱数）

```python
import random

random.randint(1, 6)        # 1〜6 の整数（両端含む）
random.choice(["a", "b"])  # 1 個選ぶ
nums = [1, 2, 3]
random.shuffle(nums)          # 元のリストの要素をシャッフル
```

パスワードやトークンなど、**セキュリティ用途の乱数**には `random` ではなく `secrets` を使う。

```python
import secrets

token = secrets.token_hex(16)
```

### `math`（数学）

```python
import math

math.sqrt(16)                # 4.0
math.ceil(2.1)               # 3
math.floor(2.9)              # 2
math.pi                      # 円周率
math.isclose(0.1 + 0.2, 0.3) # True（浮動小数点比較）
```

### `urllib.request`（シンプルな HTTP GET）

```python
from urllib.request import urlopen

with urlopen("https://example.com", timeout=5) as response:
    html = response.read().decode("utf-8")
```

HTTP エラーや接続失敗は例外になり得る。実際のプログラムではタイムアウトとエラー処理を考える。

### `logging`（ログ出力）

```python
import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logging.info("処理を開始")
logging.warning("注意が必要")
logging.error("エラーが発生")
```

---

## 31. Common Pitfalls

### `=`、`==`、`is` を混同しない

```python
x = 10                  # 代入
x == 10                # 値が等しいか
x is None              # None か（同一性比較）
```

`is` は文字列・数値の値比較には使わない。値比較は `==`。

### 可変デフォルト引数を避ける

```python
# NG: 同じリストが次回以降の呼び出しにも共有される
# def add_item(item, items=[]):
#     items.append(item)
#     return items

# OK
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
```

### 代入とコピーは違う

```python
a = [1, 2]
b = a                       # 同じリストを参照
b.append(3)
print(a)                    # [1, 2, 3]

c = a.copy()                # 浅いコピー（内側のリスト等は共有され得る）
```

### `sort()` と `sorted()`

```python
nums = [3, 1, 2]
nums.sort()                 # nums を変更、返り値は None
new_nums = sorted(nums)    # 新しいリストを返す
```

### ループ中の削除は慎重に

```python
nums = [1, 2, 3, 4]
nums = [x for x in nums if x % 2 == 0]  # 残す条件で新リストを作る
```

### 数値・文字列の混同

```python
"10" + "20"               # '1020'
10 + 20                   # 30
int("10") + int("20")     # 30
```

### 浮動小数点の誤差

```python
0.1 + 0.2 == 0.3          # False になり得る

import math
math.isclose(0.1 + 0.2, 0.3)  # True
```

### `and` / `or` は必ずしも bool を返さない

```python
name = ""
label = name or "guest"       # 'guest'
value = 0 or 100              # 100（0 も既定値に置換される）
```

**0 と未設定を区別したい**なら `if value is None` を使う。

### リストを掛け算した二次元配列に注意

```python
# NG: 内側の同じリストを共有
# grid = [[0] * 3] * 2

# OK: 行ごとに別のリストを作る
grid = [[0] * 3 for _ in range(2)]
```

### その他の基本ルール

- `input()` は **str** を返す。整数が必要なら `int()`。
- `range(5)` は `0`〜`4`。終端の `5` は含まない。
- `dict[key]` でキーがなければ `KeyError`。`dict.get(key)` も使う。
- `list[index]` が範囲外なら `IndexError`。
- 関数が何も返さなければ `None`。
- `str`、`tuple` は要素を差し替えられない。`list`、`dict`、`set` は変更可能。
- `"w"` は**上書き**。既存ファイルの内容を消したくなければ `"a"` や `"x"` を検討。
- `except Exception:` にまとめるより、具体的な例外を捕まえる。
- `assert` はデバッグ時の前提チェック向け。ユーザー入力の検証には `if` / `raise` を使う。

---

## 32. Small Script Template

**CSV を読み、指定スコア以上の人だけ表示する CLI。** `argparse`・関数・ファイル・例外・`main()` を組み合わせた最小構成。

`filter_scores.py`:

```python
#!/usr/bin/env python3
"""CSV から指定スコア以上のデータを表示する。"""

import argparse
import csv
import sys
from pathlib import Path


def load_scores(path: Path) -> list[tuple[str, int]]:
    records = []
    with path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            records.append((row["name"], int(row["score"])))
    return records


def main() -> int:
    parser = argparse.ArgumentParser(description="CSV のスコアを絞り込む")
    parser.add_argument("csv_file", type=Path, help="入力 CSV ファイル")
    parser.add_argument("--min-score", type=int, default=70)
    args = parser.parse_args()

    try:
        records = load_scores(args.csv_file)
    except (OSError, KeyError, ValueError) as exc:
        print(f"読み込みに失敗: {exc}", file=sys.stderr)
        return 1

    for name, score in records:
        if score >= args.min_score:
            print(f"{name}: {score}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
```

入力ファイル `scores.csv`:

```csv
name,score
Alice,90
Bob,65
Carol,80
```

```bash
python3 filter_scores.py scores.csv --min-score 80
# Alice: 90
# Carol: 80
```

---

## 33. Quick Reference

| やりたいこと | 代表的な書き方 |
|---|---|
| 変数に代入 | `x = 10` |
| 画面へ表示 | `print(x)` |
| 入力を受け取る | `s = input("入力: ")` |
| 文字列へ埋め込む | `f"value={x}"` |
| 条件分岐 | `if condition: ...` |
| ループ | `for x in items: ...` |
| 指定回数ループ | `for i in range(10): ...` |
| 添字付きループ | `for i, x in enumerate(items): ...` |
| 2 つを並行ループ | `for a, b in zip(xs, ys): ...` |
| 関数を作る | `def func(x): return x * 2` |
| リスト追加 | `items.append(x)` |
| リストの一部 | `items[1:4]` |
| リストを絞る | `[x for x in xs if x > 0]` |
| リストの並べ替え | `sorted(items)` |
| 辞書から取得 | `data.get("key", default)` |
| キーの存在確認 | `"key" in data` |
| 重複を除去 | `set(items)` |
| 文字列を分割 | `s.split(",")` |
| 文字列を結合 | `",".join(items)` |
| 文字列を置換 | `s.replace("old", "new")` |
| 部分文字列判定 | `"abc" in s` |
| `None` 判定 | `x is None` |
| ファイルを読む | `Path("a.txt").read_text(encoding="utf-8")` |
| ファイルを書く | `Path("a.txt").write_text(s, encoding="utf-8")` |
| ファイル一覧 | `Path(".").glob("*.txt")` |
| JSON を読む | `json.load(f)` |
| CSV を読む | `csv.DictReader(f)` |
| 例外を処理 | `try: ... except ValueError: ...` |
| CLI 引数 | `argparse.ArgumentParser()` |
| 環境変数を取得 | `os.getenv("NAME")` |
| 外部コマンド | `subprocess.run(["cmd", "arg"], check=True)` |
| プログラムの入口 | `if __name__ == "__main__": main()` |

---

## Notes

- **対象**: Python 3.10 以降（`match`、`str | None` を含む）。
- **対象外**: NumPy / pandas / Django などの外部ライブラリ、非同期処理の詳細、デコレータの自作、メタクラスなど。
- **リファレンス**: [Python 公式ドキュメント](https://docs.python.org/3/) / [Python チュートリアル（日本語）](https://docs.python.org/ja/3/tutorial/)。
- **形式の参考**: [Linux Shell Scripting Cheat Sheet](https://github.com/nekomaruv2-EthHack/WriteUpRepo/blob/main/tools/cheatsheets/shellscripts_cheetsheet.md)（見出し → 短い説明 → コード例の構成）。本文とコード例は Python 用に新規作成。
