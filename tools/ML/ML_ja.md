# Python / NumPy / 機械学習 チートシート

> Python・NumPy・機械学習コードを「自分で書く・読む・デバッグする」ための実用チートシート。
>
> 特に以下を重視しています。
>
> - よく使うPython文法
> - NumPyの配列操作
> - `shape`, `axis`, `reshape`
> - Boolean Mask
> - `stack`, `hstack`, `vstack`, `concatenate`
> - Broadcasting
> - 機械学習の前処理
> - 標準化
> - Data Leakage
> - 学習・評価でよく使う基本パターン

---

# まず困ったら確認するもの

NumPyや機械学習コードで挙動がおかしいときは、まずこれを見る。

```python
print(type(x))
print(x)
print(x.shape)
print(x.ndim)
print(x.dtype)
```

ラベルなら：

```python
print(y.shape)
print(np.unique(y, return_counts=True))
```

train/testなら：

```python
print(X_train.shape, X_test.shape)
print(y_train.shape, y_test.shape)
```

基本ルール：

```text
行 = サンプル
列 = 特徴量
```

たとえば：

```python
X.shape == (100, 5)
```

なら、

```text
100サンプル
1サンプルあたり5特徴量
```

という意味。

---

# import

よく使うもの：

```python
import numpy as np
import pandas as pd
```

機械学習：

```python
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
```

---

# 変数

```python
name = "Alice"
count = 10
score = 0.85
is_valid = True
```

Pythonでは型を明示しなくてもよい。

```python
type(name)
type(count)
```

---

# 基本型

```python
text = "hello"      # str
count = 10          # int
score = 0.8         # float
flag = True         # bool
nothing = None      # NoneType
```

型変換：

```python
int("10")
float("3.14")
str(100)
bool(1)
```

---

# 文字列

```python
text = "hello world"
```

長さ：

```python
len(text)
```

index：

```python
text[0]      # 'h'
text[-1]     # 'd'
```

slice：

```python
text[:5]     # 'hello'
text[6:]     # 'world'
```

よく使うメソッド：

```python
text.lower()
text.upper()
text.strip()
text.split()
text.replace("world", "python")
```

部分文字列を含むか：

```python
"hello" in text
```

f-string：

```python
name = "Alice"
score = 0.91

print(f"{name}: {score}")
print(f"{score:.2f}")
```

---

# list

```python
values = [10, 20, 30]
```

参照：

```python
values[0]
values[-1]
```

追加：

```python
values.append(40)
```

複数追加：

```python
values.extend([50, 60])
```

長さ：

```python
len(values)
```

削除：

```python
values.remove(20)
```

末尾を取り出して削除：

```python
last = values.pop()
```

含まれているか：

```python
30 in values
```

---

# Slice

基本形：

```python
x[start:end:step]
```

`end` は含まれない。

```python
x = [10, 20, 30, 40, 50]
```

先頭3個：

```python
x[:3]
# [10, 20, 30]
```

index 2以降：

```python
x[2:]
# [30, 40, 50]
```

途中だけ：

```python
x[1:4]
# [20, 30, 40]
```

2個おき：

```python
x[::2]
# [10, 30, 50]
```

逆順：

```python
x[::-1]
```

覚え方：

```text
[:N]   = 先頭からN個
[N:]   = N番目以降
[a:b]  = a番目からb-1番目まで
```

---

# tuple

tupleは変更不可。

```python
point = (10, 20)
```

展開：

```python
x, y = point
```

`shape` の：

```python
(100, 5)
```

もtuple。

---

# dict

```python
user = {
    "name": "Alice",
    "age": 30,
}
```

参照：

```python
user["name"]
```

安全な参照：

```python
user.get("email")
user.get("email", "unknown")
```

追加・更新：

```python
user["age"] = 31
user["email"] = "alice@example.com"
```

loop：

```python
for key, value in user.items():
    print(key, value)
```

keyだけ：

```python
user.keys()
```

valueだけ：

```python
user.values()
```

---

# set

重複排除や高速な存在確認に便利。

```python
items = {1, 2, 3}
```

追加：

```python
items.add(4)
```

存在確認：

```python
2 in items
```

listの重複排除：

```python
values = [1, 1, 2, 3, 3]
unique = set(values)
```

---

# if / elif / else

```python
if score >= 0.8:
    print("high")
elif score >= 0.5:
    print("medium")
else:
    print("low")
```

論理演算：

```python
and
or
not
```

例：

```python
if score > 0.8 and is_valid:
    print("accept")
```

---

# Truthy / Falsy

以下はFalse扱いになる。

```python
False
None
0
0.0
""
[]
{}
set()
```

例：

```python
if values:
    print("空ではない")
```

---

# for

```python
for value in [10, 20, 30]:
    print(value)
```

range：

```python
for i in range(5):
    print(i)
```

出力：

```text
0
1
2
3
4
```

開始値を指定：

```python
for i in range(2, 5):
    print(i)
```

---

# enumerate

indexとvalueを同時に使いたいとき。

```python
items = ["a", "b", "c"]

for i, item in enumerate(items):
    print(i, item)
```

出力：

```text
0 a
1 b
2 c
```

1から始める：

```python
for rank, item in enumerate(items, start=1):
    print(rank, item)
```

ランキング処理などで非常によく使う。

---

# zip

複数の配列を同時にloopする。

```python
names = ["Alice", "Bob"]
scores = [0.8, 0.9]

for name, score in zip(names, scores):
    print(name, score)
```

ペアを作る：

```python
pairs = list(zip(names, scores))
```

---

# List Comprehension

普通に書くと：

```python
result = []

for x in range(5):
    result.append(x * 2)
```

短くすると：

```python
result = [x * 2 for x in range(5)]
```

条件付き：

```python
even = [x for x in range(10) if x % 2 == 0]
```

便利だが、複雑になりすぎるなら普通のfor文の方が読みやすい。

---

# 関数

```python
def add(a, b):
    return a + b
```

default値：

```python
def greet(name="guest"):
    return f"Hello {name}"
```

keyword argument：

```python
greet(name="Alice")
```

型ヒント：

```python
def add(a: int, b: int) -> int:
    return a + b
```

型ヒントは読みやすさ向上のための情報であり、通常は実行時の型強制ではない。

---

# 複数の戻り値

```python
def min_max(values):
    return min(values), max(values)

minimum, maximum = min_max([1, 2, 3])
```

内部的にはtupleが返っている。

---

# lambda

小さな無名関数。

```python
square = lambda x: x ** 2
```

sortでよく使う：

```python
items = [
    {"name": "a", "score": 0.5},
    {"name": "b", "score": 0.9},
]

items.sort(key=lambda x: x["score"], reverse=True)
```

複雑な処理なら`def`を使う方が読みやすい。

---

# 例外処理

```python
try:
    value = int(text)
except ValueError:
    print("整数ではありません")
```

例外オブジェクトを取る：

```python
try:
    ...
except ValueError as e:
    print(e)
```

自分で例外を投げる：

```python
if score < 0:
    raise ValueError("score must be non-negative")
```

---

# pathlibでファイル操作

```python
from pathlib import Path
```

読み込み：

```python
path = Path("data.txt")
text = path.read_text(encoding="utf-8")
```

書き込み：

```python
path.write_text("hello", encoding="utf-8")
```

存在確認：

```python
path.exists()
```

ディレクトリ作成：

```python
Path("output").mkdir(parents=True, exist_ok=True)
```

---

# NumPy 基本

```python
import numpy as np
```

1次元配列：

```python
x = np.array([1, 2, 3])
```

2次元配列：

```python
X = np.array([
    [1, 2, 3],
    [4, 5, 6],
])
```

---

# shape / ndim / dtype / size

```python
X.shape
X.ndim
X.dtype
X.size
```

例：

```python
X = np.array([
    [1, 2, 3],
    [4, 5, 6],
])
```

結果：

```python
X.shape
# (2, 3)

X.ndim
# 2

X.size
# 6
```

意味：

```text
shape = (行数, 列数)
      = (サンプル数, 特徴量数)
```

---

# 1次元と2次元の違い

これらは別物。

```python
a = np.array([1, 2, 3])
a.shape
# (3,)
```

```python
b = np.array([[1, 2, 3]])
b.shape
# (1, 3)
```

```python
c = np.array([
    [1],
    [2],
    [3],
])
c.shape
# (3, 1)
```

整理：

```text
(3,)   = 1次元ベクトル
(1, 3) = 2次元・1行3列
(3, 1) = 2次元・3行1列
```

機械学習ではこの違いが非常に重要。

---

# NumPy Index

```python
x = np.array([10, 20, 30, 40])
```

先頭：

```python
x[0]
```

末尾：

```python
x[-1]
```

2次元：

```python
X = np.array([
    [10, 20],
    [30, 40],
])
```

0行1列：

```python
X[0, 1]
# 20
```

0行目：

```python
X[0]
```

0列目：

```python
X[:, 0]
```

---

# NumPy Slice

```python
x[start:end:step]
```

例：

```python
x = np.array([10, 20, 30, 40, 50])
```

```python
x[:3]
# array([10, 20, 30])
```

```python
x[2:]
# array([30, 40, 50])
```

```python
x[1:4]
# array([20, 30, 40])
```

行列：

```python
X[:3, :]
```

意味：

```text
先頭3行
全列
```

```python
X[:, :2]
```

意味：

```text
全行
先頭2列
```

---

# Boolean Mask / Boolean Indexing

NumPyで非常によく使う。

```python
a = np.array([0, 1, 0, 1])
score = np.array([0.2, 0.8, 0.4, 0.9])
```

比較：

```python
a == 1
```

結果：

```python
array([False, True, False, True])
```

このTrue/False配列をindexとして使える。

```python
score[a == 1]
```

結果：

```python
array([0.8, 0.9])
```

意味：

```text
a == 1 の場所に対応する score だけ取る
```

---

# Boolean条件を複数使う

AND：

```python
score[(a == 1) & (score > 0.8)]
```

OR：

```python
score[(a == 1) | (score > 0.8)]
```

NOT：

```python
score[~(a == 1)]
```

重要：

```python
# NumPyでは基本NG
(a == 1) and (score > 0.8)

# NumPyではこちら
(a == 1) & (score > 0.8)
```

条件ごとに必ず括弧をつける。

---

# Fancy Indexing

特定のindexだけ取る。

```python
x = np.array([10, 20, 30, 40])

x[[0, 2]]
# array([10, 30])
```

行列の特定行：

```python
X[[0, 3, 5]]
```

---

# np.where

条件に一致するindexを取る：

```python
indices = np.where(score > 0.5)
```

条件で値を置き換える：

```python
result = np.where(score > 0.5, 1, 0)
```

これは：

```text
条件がTrueなら1
Falseなら0
```

という意味。

---

# axis

NumPyで特に重要。

```python
X = np.array([
    [1, 2, 3],
    [4, 5, 6],
])
```

shape：

```python
X.shape
# (2, 3)
```

考え方：

```text
axis=0
→ 行方向をつぶす
→ 各列について結果が出る

axis=1
→ 列方向をつぶす
→ 各行について結果が出る
```

列ごとの平均：

```python
X.mean(axis=0)
```

結果：

```python
array([2.5, 3.5, 4.5])
```

行ごとの平均：

```python
X.mean(axis=1)
```

結果：

```python
array([2., 5.])
```

覚え方：

```text
axis=0 → 縦に計算して列ごとの結果
axis=1 → 横に計算して行ごとの結果
```

---

# 集約処理

```python
np.sum(X)
np.mean(X)
np.std(X)
np.min(X)
np.max(X)
```

列ごと：

```python
X.mean(axis=0)
```

行ごと：

```python
X.mean(axis=1)
```

次元を維持：

```python
X.mean(axis=0, keepdims=True)
```

`keepdims=False`なら：

```text
(1, 3) → (3,)
```

`keepdims=True`なら：

```text
(1, 3)
```

Broadcastingで便利。

---

# reshape

要素数を変えずに形を変える。

```python
x = np.array([1, 2, 3, 4, 5, 6])
```

```python
x.reshape(2, 3)
```

結果：

```python
array([
    [1, 2, 3],
    [4, 5, 6],
])
```

`-1` は：

```text
NumPy側で自動計算
```

という意味。

```python
x.reshape(-1, 1)
```

結果：

```text
(6, 1)
```

1次元配列を「1特徴量の複数サンプル」に変換するときによく使う。

---

# ravel / flatten

1次元化：

```python
X.ravel()
```

```python
X.flatten()
```

違い：

```text
ravel()   可能ならview
flatten() 必ずcopy
```

---

# squeeze

サイズ1の次元を削除。

```python
x.shape
# (100, 1)
```

```python
x.squeeze().shape
# (100,)
```

指定：

```python
x.squeeze(axis=1)
```

`(1, 1, N)`のような配列に無指定で使うと、意図以上に次元が消えることがある。

---

# 次元を追加する

```python
x = np.array([1, 2, 3])
```

列ベクトル風：

```python
x[:, np.newaxis]
# shape (3, 1)
```

行ベクトル風：

```python
x[np.newaxis, :]
# shape (1, 3)
```

同じこと：

```python
np.expand_dims(x, axis=1)
```

---

# 転置

```python
X.T
```

例：

```python
X.shape
# (2, 3)

X.T.shape
# (3, 2)
```

ただし1次元では：

```python
x.shape
# (3,)

x.T.shape
# (3,)
```

1次元配列には「行・列」という向きがないので、`.T`しても変わらない。

`(1, 3)` や `(3, 1)` にしたいなら `reshape` を使う。

---

# np.concatenate

既存のaxisに沿って結合。

```python
A = np.array([
    [1, 2],
    [3, 4],
])

B = np.array([
    [5, 6],
    [7, 8],
])
```

縦結合：

```python
np.concatenate([A, B], axis=0)
```

shape：

```text
(2, 2) + (2, 2) → (4, 2)
```

横結合：

```python
np.concatenate([A, B], axis=1)
```

shape：

```text
(2, 2) + (2, 2) → (2, 4)
```

---

# np.vstack

Vertical Stack。

縦に積む。

```python
np.vstack([A, B])
```

イメージ：

```text
A
B
```

---

# np.hstack

Horizontal Stack。

横につなぐ。

```python
np.hstack([A, B])
```

イメージ：

```text
A B
```

特徴量をまとめる例：

```python
feature_a = np.array([[0.1], [0.2], [0.3]])
feature_b = np.array([[10], [20], [30]])

X = np.hstack([feature_a, feature_b])
```

結果：

```python
array([
    [0.1, 10.0],
    [0.2, 20.0],
    [0.3, 30.0],
])
```

shape：

```text
(3, 1) + (3, 1) → (3, 2)
```

---

# np.stack

`concatenate`との重要な違い：

```text
stackは新しいaxisを作る
```

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
```

```python
np.stack([a, b])
```

shape：

```text
(3,) + (3,) → (2, 3)
```

```python
np.stack([a, b], axis=1)
```

なら：

```text
(3, 2)
```

---

# stack系まとめ

```text
concatenate
→ 既存axisに沿って結合

hstack
→ 横方向に結合

vstack
→ 縦方向に結合

stack
→ 新しい次元を作って積む
```

迷ったら必ず：

```python
print(A.shape)
print(B.shape)
```

を見る。

---

# np.column_stack

1次元配列を特徴量列としてまとめるとき便利。

```python
a = np.array([1, 2, 3])
b = np.array([10, 20, 30])

X = np.column_stack([a, b])
```

結果：

```python
array([
    [1, 10],
    [2, 20],
    [3, 30],
])
```

shape：

```text
(3, 2)
```

`reshape(-1, 1)` + `hstack` の代わりとして便利。

---

# Broadcasting

形の違う配列同士をNumPyがうまく計算してくれる仕組み。

```python
X = np.array([
    [1, 2, 3],
    [4, 5, 6],
])

mean = np.array([2.5, 3.5, 4.5])

X - mean
```

shape：

```text
X    : (2, 3)
mean : (3,)
```

NumPyは概念的に：

```text
meanを各行に適用
```

してくれる。

そのため：

```python
X_standardized = (X - mean) / std
```

のような計算ができる。

---

# Broadcastingの基本ルール

右端の次元から比較する。

次元が以下なら互換性あり：

```text
同じサイズ
または
どちらかが1
```

例：

```text
(100, 5)
(5,)
```

は互換。

```text
(100, 5)
(1, 5)
```

も互換。

一方：

```text
(100, 5)
(100,)
```

は意図した動作にならないことが多い。

---

# copy と view

NumPyのsliceはviewになることがある。

```python
x = np.array([1, 2, 3, 4])

part = x[:2]
part[0] = 999
```

このとき元の`x`も変わる場合がある。

独立した配列が欲しいなら：

```python
part = x[:2].copy()
```

---

# sort / argsort

値をsort：

```python
np.sort(scores)
```

sortしたときのindex：

```python
np.argsort(scores)
```

降順：

```python
np.argsort(scores)[::-1]
```

Top 3：

```python
top3 = np.argsort(scores)[::-1][:3]
```

ランキング処理で頻出。

---

# argmax / argmin

最大値のindex：

```python
np.argmax(scores)
```

最小値：

```python
np.argmin(scores)
```

行列なら：

```python
np.argmax(X, axis=1)
```

各行について最大の列indexを返す。

分類でよくある：

```python
predicted_class = np.argmax(logits, axis=1)
```

---

# np.unique

unique値：

```python
np.unique(y)
```

件数も：

```python
values, counts = np.unique(y, return_counts=True)
```

分類ラベルの偏り確認に便利。

---

# 乱数

推奨：

```python
rng = np.random.default_rng(42)
```

乱数：

```python
rng.random(5)
```

整数：

```python
rng.integers(0, 10, size=5)
```

shuffle：

```python
rng.shuffle(x)
```

固定seedを使うと再現性を確保しやすい。

---

# 行列積

要素ごとの積：

```python
A * B
```

行列積：

```python
A @ B
```

または：

```python
np.matmul(A, B)
```

内積：

```python
np.dot(a, b)
```

機械学習ではshapeを常に意識する。

例：

```text
X: (100, 5)
W: (5, 3)

X @ W → (100, 3)
```

---

# 線形モデルのshape

典型：

```python
logits = X @ W + b
```

shape：

```text
X      : (N, D)
W      : (D, C)
b      : (C,)
logits : (N, C)
```

意味：

```text
N = サンプル数
D = 特徴量数
C = クラス数
```

---

# Pandas 基本

```python
df = pd.DataFrame({
    "name": ["Alice", "Bob"],
    "score": [0.8, 0.9],
})
```

確認：

```python
df.head()
df.shape
df.columns
df.dtypes
df.info()
df.describe()
```

1列：

```python
df["score"]
```

複数列：

```python
df[["name", "score"]]
```

条件抽出：

```python
df[df["score"] > 0.8]
```

複数条件：

```python
df[(df["score"] > 0.8) & (df["name"] != "Alice")]
```

---

# loc / iloc

labelで指定：

```python
df.loc[0, "score"]
```

位置で指定：

```python
df.iloc[0, 1]
```

覚え方：

```text
loc  = label
iloc = integer position
```

---

# 欠損値

確認：

```python
df.isna().sum()
```

削除：

```python
df.dropna()
```

埋める：

```python
df["score"] = df["score"].fillna(0)
```

欠損値は意味を考えずに0埋めしない。

---

# 機械学習での X と y

基本：

```text
X = 入力特徴量
y = 正解ラベル / target
```

例：

```python
X = np.array([
    [0.8, 10.0],
    [0.3,  2.0],
    [0.7,  8.0],
])

y = np.array([1, 0, 1])
```

shape：

```text
X.shape → (3, 2)
y.shape → (3,)
```

---

# Train / Validation / Test

役割：

```text
train
→ パラメータを学習

validation
→ モデルやハイパーパラメータを比較

test
→ 最終評価
```

簡単なtrain/test：

```python
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
)
```

分類では：

```python
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y,
)
```

`stratify=y`でクラス比率を維持しやすい。

---

# 標準化 Standardization

標準化は「特徴量ごと」に行う。

式：

```text
z = (x - 平均) / 標準偏差
```

重要：

```text
異なる特徴量を全部まとめて平均するのではない
```

たとえば：

```text
列0 = 特徴量A
列1 = 特徴量B
列2 = 特徴量C
```

なら、それぞれ別に：

```text
平均
標準偏差
```

を計算する。

NumPy：

```python
mean = X_train.mean(axis=0)
std = X_train.std(axis=0)

X_train_std = (X_train - mean) / std
X_test_std = (X_test - mean) / std
```

ここで：

```python
axis=0
```

なので列ごとの平均・標準偏差になる。

重要：

```text
平均・標準偏差はtrainだけから計算する
```

---

# StandardScaler

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
```

基本：

```text
train → fit_transform
test  → transform
```

testで：

```python
scaler.fit_transform(X_test)
```

してはいけない。

test側の情報を前処理に使ってしまうため。

---

# 標準化とMin-Max Scalingの違い

標準化：

```text
平均 ≒ 0
標準偏差 ≒ 1
```

Min-Max Scaling：

```text
通常 0〜1 に収める
```

例：

```python
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
```

---

# 標準化とベクトル正規化の違い

別物。

標準化：

```text
同じ特徴量を複数サンプル間で比較
```

例：

```text
feature A列の平均・標準偏差を使う
```

ベクトル正規化：

```text
1サンプル内のベクトル全体を処理
```

L2 normalization：

```python
from sklearn.preprocessing import normalize

X_norm = normalize(X, norm="l2")
```

各ベクトルの長さを1にする。

---

# 標準化が効きやすいモデル

よく効果がある：

```text
ロジスティック回帰
SVM
k-NN
k-means
ニューラルネットワーク
PCA
距離ベースの手法
```

比較的影響が小さい：

```text
Decision Tree
Random Forest
Gradient Boosting Tree
```

理由：

```text
距離や勾配を使うモデル
→ 値のスケールの影響を受けやすい

木モデル
→ 値の大小関係・閾値分割が中心
```

---

# 0/1特徴量

```text
0 / 1
```

のようなbinary flagは、必ずしも標準化しなくてよい。

例：

```text
連続値A
連続値B
0/1フラグ
```

なら、

```text
連続値だけ標準化
0/1はそのまま
```

とすることも多い。

---

# Data Leakage

本来未知であるtestデータの情報がtraining側に漏れること。

悪い例：

```python
scaler.fit(X)
X_scaled = scaler.transform(X)

X_train, X_test, ... = train_test_split(X_scaled, ...)
```

問題：

```text
scalerがtestデータも見ている
```

正しい流れ：

```python
X_train, X_test, y_train, y_test = train_test_split(...)

scaler.fit(X_train)

X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)
```

基本ルール：

```text
splitを先にする

前処理のfitはtrainだけ

validation/testはtransformだけ
```

---

# Pipeline

前処理とモデルをまとめる。

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

model = Pipeline([
    ("scaler", StandardScaler()),
    ("classifier", LogisticRegression()),
])

model.fit(X_train, y_train)
pred = model.predict(X_test)
```

メリット：

```text
Data Leakageを防ぎやすい
コードが短い
Cross Validationしやすい
```

---

# Baselineを先に作る

基本：

```text
baseline
↓
評価
↓
1つ変更
↓
再評価
```

いきなり：

```text
モデル変更
特徴量追加
前処理変更
Loss変更
threshold変更
```

を全部やると、何が効いたのかわからなくなる。

---

# fit / transform / predict

よく使う意味：

```text
fit
→ データからパラメータを学習

transform
→ 学習済み変換を適用

predict
→ 予測する
```

例：

```python
scaler.fit(X_train)
X_scaled = scaler.transform(X_train)
```

```python
model.fit(X_train, y_train)
pred = model.predict(X_test)
```

---

# fit_transform

これは：

```python
transformer.fit(X)
transformer.transform(X)
```

を一度にやる。

```python
X2 = transformer.fit_transform(X)
```

通常はtrain側で使う。

---

# predict_proba

分類器によっては：

```python
proba = model.predict_proba(X_test)
```

shape：

```text
(N, C)
```

2クラスなら：

```python
positive_probability = proba[:, 1]
```

---

# Accuracy

```text
全予測のうち何件正解したか
```

式：

```text
正解数 / 全件数
```

クラス不均衡があると誤解を招くことがある。

---

# Precision

```text
Positiveと予測したもののうち、
本当にPositiveだった割合
```

式：

```text
TP / (TP + FP)
```

False Positiveを減らしたいとき重要。

---

# Recall

```text
本当のPositiveのうち、
どれだけ拾えたか
```

式：

```text
TP / (TP + FN)
```

見逃しを減らしたいとき重要。

---

# F1 Score

PrecisionとRecallの調和平均。

```text
F1 =
2 * Precision * Recall
/
(Precision + Recall)
```

両方をバランスよく見たいときに使う。

---

# scikit-learnで評価

```python
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
)

accuracy = accuracy_score(y_test, pred)
precision = precision_score(y_test, pred)
recall = recall_score(y_test, pred)
f1 = f1_score(y_test, pred)
```

---

# Confusion Matrix

```python
from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_test, pred)
```

2クラス：

```text
[[TN, FP],
 [FN, TP]]
```

どの種類の誤りが多いか確認できる。

---

# Class Imbalance

確認：

```python
np.unique(y, return_counts=True)
```

または：

```python
pd.Series(y).value_counts()
```

1クラスが極端に多いと：

```text
Accuracyが高い
```

だけではモデル性能がよいとは限らない。

見るべき候補：

```text
Precision
Recall
F1
Confusion Matrix
```

---

# 再現性

比較実験では乱数seedを固定する。

```python
random_state=42
```

NumPy：

```python
rng = np.random.default_rng(42)
```

実験条件を変えたとき、乱数の影響を減らせる。

---

# Overfitting

典型：

```text
train性能      非常に高い
validation性能 低い
```

原因候補：

```text
モデルが複雑すぎる
データが少ない
特徴量が多すぎる
Data Leakage
epochが多すぎる
```

---

# Underfitting

典型：

```text
train性能      低い
validation性能 低い
```

原因候補：

```text
モデルが単純すぎる
特徴量不足
学習不足
正則化が強すぎる
```

---

# Feature Engineering

Feature = モデルへの入力となる特徴量。

例：

```text
長さ
回数
類似度
0/1フラグ
頻度
カテゴリ
```

基本：

```text
1行 = 1サンプル
1列 = 1特徴量
```

---

# Feature Scale

例：

```text
特徴量A: 0.0〜1.0
特徴量B: 0〜10000
```

スケールに敏感なモデルでは、Bが数値的に大きいだけで強く効くことがある。

そこで標準化を使う。

---

# Cosine Similarity

ベクトル `a`, `b`：

```text
cosine similarity =
(a · b) / (||a|| ||b||)
```

NumPy：

```python
cos_sim = np.dot(a, b) / (
    np.linalg.norm(a) * np.linalg.norm(b)
)
```

すでにL2 normalization済みなら：

```text
cosine similarity = dot product
```

---

# Euclidean Distance

```python
distance = np.linalg.norm(a - b)
```

小さいほど近い。

Cosine Similarityはベクトルの「向き」を重視する。

---

# Softmax

logitを確率らしい値に変える。

```python
def softmax(x):
    x = x - np.max(x, axis=-1, keepdims=True)
    exp_x = np.exp(x)
    return exp_x / np.sum(exp_x, axis=-1, keepdims=True)
```

最大値を引くのは数値安定性のため。

---

# Logit

Softmax前の生スコア。

```python
logits = np.array([2.0, 0.5, -1.0])
```

まだ確率ではない。

Softmax：

```python
probs = softmax(logits)
```

すると：

```python
probs.sum()
# 約1
```

---

# Cross Entropy

正解クラスに割り当てた確率を使う。

概念：

```text
正解クラス確率が高い
→ Loss小

正解クラス確率が低い
→ Loss大
```

代表式：

```text
loss = -log(正解クラス確率)
```

---

# Margin Ranking の考え方

ランキングでは：

```text
positive_score
>
negative_score + margin
```

となってほしい。

代表例：

```text
loss = max(
    0,
    margin - positive_score + negative_score
)
```

十分差が開いていれば：

```text
loss = 0
```

---

# Hard Negative

Hard Negativeとは：

```text
不正解だが、
正解にかなり似ていて区別が難しいデータ
```

Easy Negative：

```text
明らかに無関係
```

Hard Negative：

```text
単語が似ている
特徴量が似ている
文脈が似ている
しかし不正解
```

Hard Negativeは学習を強くできるが、ラベルミスや曖昧なデータを入れすぎると逆効果。

---

# Top-K

```python
scores = np.array([0.3, 0.9, 0.6, 0.8])
```

上位K件：

```python
k = 2
top_k = np.argsort(scores)[::-1][:k]
```

scoreを取る：

```python
top_scores = scores[top_k]
```

---

# 特徴量をまとめるときのshape

```python
feature_a.shape
# (100,)

feature_b.shape
# (100,)
```

これをそのまま：

```python
np.hstack([feature_a, feature_b])
```

すると：

```text
(200,)
```

になる。

欲しいものが：

```text
100サンプル × 2特徴量
```

なら：

```python
feature_a = feature_a.reshape(-1, 1)
feature_b = feature_b.reshape(-1, 1)

X = np.hstack([feature_a, feature_b])
```

結果：

```text
X.shape == (100, 2)
```

または：

```python
X = np.column_stack([feature_a, feature_b])
```

---

# yのshape

多くのscikit-learn APIでは：

```text
X: (N, D)
y: (N,)
```

を期待する。

もし：

```text
y: (N, 1)
```

なら：

```python
y = y.ravel()
```

---

# 1サンプルだけpredictする

```python
x = np.array([0.5, 1.2, 3.0])
```

shape：

```text
(3,)
```

scikit-learnは通常：

```text
(samples, features)
```

を期待する。

なので：

```python
x = x.reshape(1, -1)
```

shape：

```text
(1, 3)
```

その後：

```python
model.predict(x)
```

---

# 1特徴量・複数サンプル

```python
x = np.array([10, 20, 30, 40])
```

これが：

```text
4サンプル
1特徴量
```

なら：

```python
X = x.reshape(-1, 1)
```

shape：

```text
(4, 1)
```

---

# サンプル数が一致しているか

NG：

```text
X.shape = (100, 5)
y.shape = (99,)
```

基本：

```text
X.shape[0] == y.shape[0]
```

確認：

```python
assert X.shape[0] == y.shape[0]
```

---

# assert

バグの早期発見に便利。

```python
assert X.ndim == 2
assert y.ndim == 1
assert X.shape[0] == y.shape[0]
```

有限値確認：

```python
assert np.isfinite(X).all()
```

---

# NaN / inf

NaN確認：

```python
np.isnan(X).any()
```

有限値のみか：

```python
np.isfinite(X).all()
```

NaN件数：

```python
np.isnan(X).sum()
```

NaNは学習やLossを壊す原因になりやすい。

---

# 0除算

例えば：

```python
x / std
```

で：

```text
std == 0
```

だと危険。

対策：

```python
std = np.where(std == 0, 1, std)
```

標準偏差0の特徴量は全サンプル同じ値なので、そもそも情報量がないことが多い。

---

# shapeをログに出す

デバッグ中は：

```python
print("X:", X.shape)
print("y:", y.shape)
print("W:", W.shape)
print("logits:", logits.shape)
```

を入れるとよい。

機械学習コードのバグはshape由来が非常に多い。

---

# Python組み込み関数

```python
len(x)
sum(x)
min(x)
max(x)
sorted(x)
any(x)
all(x)
```

例：

```python
any(score > 0.8 for score in scores)
```

---

# sorted と .sort()

新しいlistを返す：

```python
new_values = sorted(values)
```

元listを書き換える：

```python
values.sort()
```

降順：

```python
sorted(values, reverse=True)
```

---

# dictをscoreでsort

```python
items = [
    {"name": "a", "score": 0.4},
    {"name": "b", "score": 0.9},
]
```

```python
items = sorted(
    items,
    key=lambda item: item["score"],
    reverse=True,
)
```

---

# map / filter

使えるが：

```python
result = list(map(lambda x: x * 2, values))
```

List Comprehensionの方が読みやすいことが多い：

```python
result = [x * 2 for x in values]
```

filterも：

```python
positive = [x for x in values if x > 0]
```

の方が直感的。

---

# Unpacking

```python
a, b = [10, 20]
```

不要な値：

```python
a, _ = [10, 20]
```

途中をまとめる：

```python
first, *middle, last = [1, 2, 3, 4, 5]
```

---

# *args

可変個の位置引数。

```python
def add_all(*values):
    return sum(values)
```

```python
add_all(1, 2, 3)
```

---

# **kwargs

可変個のkeyword argument。

```python
def show(**kwargs):
    print(kwargs)
```

```python
show(name="Alice", score=0.9)
```

---

# dataclass

設定値や構造化データに便利。

```python
from dataclasses import dataclass

@dataclass
class Config:
    learning_rate: float
    epochs: int
```

```python
config = Config(
    learning_rate=0.01,
    epochs=10,
)
```

---

# NumPyの型ヒント

```python
def normalize(values: np.ndarray) -> np.ndarray:
    ...
```

大きめのコードでは型ヒントが読みやすさに効く。

---

# scikit-learn 基本形

```python
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y,
)

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = LogisticRegression()
model.fit(X_train, y_train)

pred = model.predict(X_test)

print(classification_report(y_test, pred))
```

---

# Pipeline版

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("model", LogisticRegression()),
])

pipeline.fit(X_train, y_train)

pred = pipeline.predict(X_test)
```

メリット：

```text
前処理コードが減る
Data Leakageしにくい
Cross Validationしやすい
本番適用しやすい
```

---

# Cross Validation

```python
from sklearn.model_selection import cross_val_score

scores = cross_val_score(
    model,
    X,
    y,
    cv=5,
)
```

1回のtrain/test splitだけでは評価が不安定なときに使う。

最終testデータを何度もモデル選択に使わない。

---

# Threshold

binary classifierでは：

```text
0.5
```

を境界にすることが多い。

しかし目的によって変えてよい。

```python
proba = model.predict_proba(X_test)[:, 1]

pred = (proba >= 0.7).astype(int)
```

thresholdを上げると一般に：

```text
Precision ↑
Recall ↓
```

方向に動きやすい。

---

# モデル性能が悪いときの確認順

```text
1. ラベルは正しいか
2. train/test splitは正しいか
3. Data Leakageはないか
4. shapeは正しいか
5. 特徴量は意味があるか
6. クラス不均衡はないか
7. 前処理は適切か
8. baselineはどの程度か
9. Overfittingしていないか
10. 評価指標は目的に合っているか
```

---

# 実験の基本

1回に大きな変更を1つだけ。

良い例：

```text
baseline
↓
標準化追加
↓
比較
↓
特徴量を1つ追加
↓
比較
```

悪い例：

```text
モデル変更
特徴量変更
前処理変更
Loss変更
Threshold変更
```

を全部同時にやる。

---

# NumPyでよくあるミス

## `(N,)` と `(N,1)` を混同

```python
x.shape
# (100,)
```

と：

```python
x.reshape(-1, 1).shape
# (100, 1)
```

は別物。

---

## axisを間違える

まず：

```python
X.shape
```

を見る。

そのうえで：

```text
列ごとに結果が欲しい
→ axis=0

行ごとに結果が欲しい
→ axis=1
```

---

## NumPy配列にandを使う

NG：

```python
(a > 0) and (a < 1)
```

OK：

```python
(a > 0) & (a < 1)
```

---

## 条件式の括弧を忘れる

推奨：

```python
(a > 0) & (a < 1)
```

避ける：

```python
a > 0 & a < 1
```

演算子優先順位で意図しない動作になる。

---

## hstackで1次元配列をそのまま結合

```python
a.shape
# (100,)

b.shape
# (100,)
```

これを：

```python
np.hstack([a, b])
```

すると：

```text
(200,)
```

になる。

欲しいのが：

```text
(100, 2)
```

なら：

```python
np.column_stack([a, b])
```

が簡単。

---

# shapeの考え方

```text
X.shape = (N, D)
```

なら：

```text
N = サンプル数
D = 1サンプルを表す特徴量数
```

```text
logits.shape = (N, C)
```

なら：

```text
N = サンプル数
C = クラス数
```

この考え方があると、機械学習コードがかなり読みやすくなる。

---

# 学習前チェック

```text
[ ] Xとyのサンプル数は一致している
[ ] splitしてから前処理をfitしている
[ ] クラスバランスを確認した
[ ] NaN / infを確認した
[ ] 特徴量の意味を説明できる
[ ] baselineを記録した
```

---

# 実装中チェック

```text
[ ] 重要な箇所でshapeをprintした
[ ] (N,) と (N,1) を区別している
[ ] axis=0 / axis=1 を確認した
[ ] Boolean Maskに括弧をつけた
[ ] stack後のshapeを確認した
```

---

# 評価時チェック

```text
[ ] 目的に合った評価指標を使っている
[ ] baselineと比較している
[ ] 必要ならConfusion Matrixを見た
[ ] final testを何度も調整に使っていない
[ ] 1回に大きな変更を1つだけ行った
```

---

# 超短縮リファレンス

```python
# 先頭N個
x[:N]

# N番目以降
x[N:]

# Boolean Filter
x[condition]

# 複数条件
x[(a > 0) & (a < 1)]

# 0列目
X[:, 0]

# 先頭3行
X[:3, :]

# shape
X.shape

# 1列にする
x.reshape(-1, 1)

# 1サンプルにする
x.reshape(1, -1)

# 列ごとの平均
X.mean(axis=0)

# 行ごとの平均
X.mean(axis=1)

# 特徴量を列として結合
np.column_stack([a, b])

# 縦結合
np.vstack([A, B])

# 横結合
np.hstack([A, B])

# 新しいaxisを作って積む
np.stack([a, b])

# Top-K
idx = np.argsort(scores)[::-1][:k]

# 最大値index
idx = np.argmax(scores)

# unique値と件数
np.unique(y, return_counts=True)

# 行列積
X @ W

# 標準化
X_scaled = (X - mean) / std
```
