# Python / NumPy / Machine Learning Cheat Sheet

> A practical cheat sheet for writing, reading, and debugging Python code used in data processing and machine learning.
>
> Focus:
> - Python syntax you use often
> - NumPy indexing and shape manipulation
> - `axis`, `reshape`, `stack`, broadcasting
> - common machine learning preprocessing
> - avoiding data leakage and shape bugs
> - practical scikit-learn patterns

---

# Quick Debug Checklist

When NumPy / ML code behaves strangely, check these first:

```python
print(type(x))
print(x)
print(x.shape)
print(x.ndim)
print(x.dtype)
```

For labels:

```python
print(y.shape)
print(np.unique(y, return_counts=True))
```

For train/test data:

```python
print(X_train.shape, X_test.shape)
print(y_train.shape, y_test.shape)
```

Typical rule:

```text
rows    = samples
columns = features
```

Example:

```python
X.shape == (100, 5)
```

means:

```text
100 samples
5 features per sample
```

---

# Imports

Common imports:

```python
import numpy as np
import pandas as pd
```

Machine learning:

```python
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
```

---

# Variables

```python
name = "Alice"
count = 10
score = 0.85
is_valid = True
```

Python decides the type dynamically:

```python
type(name)
type(count)
```

---

# Basic Types

```python
text = "hello"      # str
count = 10          # int
score = 0.8         # float
flag = True         # bool
nothing = None      # NoneType
```

Conversions:

```python
int("10")
float("3.14")
str(100)
bool(1)
```

---

# Strings

```python
text = "hello world"
```

Length:

```python
len(text)
```

Index:

```python
text[0]      # 'h'
text[-1]     # 'd'
```

Slice:

```python
text[:5]     # 'hello'
text[6:]     # 'world'
```

Useful methods:

```python
text.lower()
text.upper()
text.strip()
text.split()
text.replace("world", "python")
```

Check substring:

```python
"hello" in text
```

f-string:

```python
name = "Alice"
score = 0.91

print(f"{name}: {score}")
print(f"{score:.2f}")
```

---

# Lists

Create:

```python
values = [10, 20, 30]
```

Access:

```python
values[0]
values[-1]
```

Append:

```python
values.append(40)
```

Extend:

```python
values.extend([50, 60])
```

Length:

```python
len(values)
```

Remove:

```python
values.remove(20)
```

Pop:

```python
last = values.pop()
```

Membership:

```python
30 in values
```

---

# List Slicing

General syntax:

```python
x[start:end:step]
```

`end` is not included.

```python
x = [10, 20, 30, 40, 50]
```

First 3:

```python
x[:3]
# [10, 20, 30]
```

From index 2 onward:

```python
x[2:]
# [30, 40, 50]
```

Middle:

```python
x[1:4]
# [20, 30, 40]
```

Every second element:

```python
x[::2]
# [10, 30, 50]
```

Reverse:

```python
x[::-1]
```

---

# Tuples

Tuples are immutable.

```python
point = (10, 20)
```

Unpacking:

```python
x, y = point
```

A shape such as:

```python
(100, 5)
```

is also a tuple.

---

# Dictionaries

```python
user = {
    "name": "Alice",
    "age": 30,
}
```

Access:

```python
user["name"]
```

Safe access:

```python
user.get("email")
user.get("email", "unknown")
```

Add/update:

```python
user["age"] = 31
user["email"] = "alice@example.com"
```

Loop:

```python
for key, value in user.items():
    print(key, value)
```

Keys:

```python
user.keys()
```

Values:

```python
user.values()
```

---

# Sets

Useful for uniqueness and membership tests.

```python
items = {1, 2, 3}
```

Add:

```python
items.add(4)
```

Membership:

```python
2 in items
```

Unique values from a list:

```python
values = [1, 1, 2, 3, 3]
unique = set(values)
```

---

# `if / elif / else`

```python
if score >= 0.8:
    print("high")
elif score >= 0.5:
    print("medium")
else:
    print("low")
```

Logical operators:

```python
and
or
not
```

Example:

```python
if score > 0.8 and is_valid:
    print("accept")
```

---

# Truthy / Falsy

Falsy values include:

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

Example:

```python
if values:
    print("not empty")
```

---

# `for`

```python
for value in [10, 20, 30]:
    print(value)
```

Range:

```python
for i in range(5):
    print(i)
```

Output:

```text
0
1
2
3
4
```

Start/end:

```python
for i in range(2, 5):
    print(i)
```

---

# `enumerate`

Use when you need both index and value.

```python
items = ["a", "b", "c"]

for i, item in enumerate(items):
    print(i, item)
```

Output:

```text
0 a
1 b
2 c
```

Start from 1:

```python
for rank, item in enumerate(items, start=1):
    print(rank, item)
```

---

# `zip`

Loop over multiple sequences together:

```python
names = ["Alice", "Bob"]
scores = [0.8, 0.9]

for name, score in zip(names, scores):
    print(name, score)
```

Create pairs:

```python
pairs = list(zip(names, scores))
```

---

# List Comprehension

Normal loop:

```python
result = []

for x in range(5):
    result.append(x * 2)
```

Equivalent:

```python
result = [x * 2 for x in range(5)]
```

With condition:

```python
even = [x for x in range(10) if x % 2 == 0]
```

Useful, but avoid deeply nested comprehensions if readability suffers.

---

# Functions

```python
def add(a, b):
    return a + b
```

Default argument:

```python
def greet(name="guest"):
    return f"Hello {name}"
```

Keyword arguments:

```python
greet(name="Alice")
```

Type hints:

```python
def add(a: int, b: int) -> int:
    return a + b
```

Type hints improve readability but are not runtime type enforcement by default.

---

# Multiple Return Values

```python
def min_max(values):
    return min(values), max(values)

minimum, maximum = min_max([1, 2, 3])
```

Python returns a tuple.

---

# `lambda`

Small anonymous function:

```python
square = lambda x: x ** 2
```

Often used for sorting:

```python
items = [
    {"name": "a", "score": 0.5},
    {"name": "b", "score": 0.9},
]

items.sort(key=lambda x: x["score"], reverse=True)
```

Prefer `def` when logic becomes non-trivial.

---

# Exceptions

```python
try:
    value = int(text)
except ValueError:
    print("invalid integer")
```

Catch exception object:

```python
try:
    ...
except ValueError as e:
    print(e)
```

Raise:

```python
if score < 0:
    raise ValueError("score must be non-negative")
```

---

# Files

Read text:

```python
from pathlib import Path

path = Path("data.txt")
text = path.read_text(encoding="utf-8")
```

Write text:

```python
path.write_text("hello", encoding="utf-8")
```

Check existence:

```python
path.exists()
```

Create directory:

```python
Path("output").mkdir(parents=True, exist_ok=True)
```

---

# NumPy Basics

Import:

```python
import numpy as np
```

Create array:

```python
x = np.array([1, 2, 3])
```

2D array:

```python
X = np.array([
    [1, 2, 3],
    [4, 5, 6],
])
```

---

# `shape`, `ndim`, `dtype`, `size`

```python
X.shape
X.ndim
X.dtype
X.size
```

Example:

```python
X = np.array([
    [1, 2, 3],
    [4, 5, 6],
])
```

Results:

```python
X.shape
# (2, 3)

X.ndim
# 2

X.size
# 6
```

Meaning:

```text
shape = (rows, columns)
      = (samples, features)
```

---

# 1D vs 2D

These are different:

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

And:

```python
c = np.array([
    [1],
    [2],
    [3],
])
c.shape
# (3, 1)
```

Remember:

```text
(3,)   = 1D vector
(1, 3) = 2D row matrix
(3, 1) = 2D column matrix
```

These distinctions matter in matrix multiplication and ML APIs.

---

# NumPy Indexing

```python
x = np.array([10, 20, 30, 40])
```

Single element:

```python
x[0]
```

Last element:

```python
x[-1]
```

2D:

```python
X = np.array([
    [10, 20],
    [30, 40],
])
```

Access row 0, column 1:

```python
X[0, 1]
# 20
```

First row:

```python
X[0]
```

First column:

```python
X[:, 0]
```

---

# NumPy Slicing

```python
x[start:end:step]
```

Example:

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

For matrices:

```python
X[:3, :]
```

means:

```text
first 3 rows
all columns
```

```python
X[:, :2]
```

means:

```text
all rows
first 2 columns
```

---

# Boolean Mask

One of the most useful NumPy patterns.

```python
a = np.array([0, 1, 0, 1])
score = np.array([0.2, 0.8, 0.4, 0.9])
```

Comparison:

```python
a == 1
```

Result:

```python
array([False, True, False, True])
```

Use the boolean array as an index:

```python
score[a == 1]
```

Result:

```python
array([0.8, 0.9])
```

Meaning:

```text
select values from score
where a equals 1
```

---

# Multiple Boolean Conditions

AND:

```python
score[(a == 1) & (score > 0.8)]
```

OR:

```python
score[(a == 1) | (score > 0.8)]
```

NOT:

```python
score[~(a == 1)]
```

Important:

```python
# Wrong for NumPy arrays
(a == 1) and (score > 0.8)

# Correct
(a == 1) & (score > 0.8)
```

Use parentheses around each condition.

---

# Fancy Indexing

Select specific positions:

```python
x = np.array([10, 20, 30, 40])

x[[0, 2]]
# array([10, 30])
```

With matrix rows:

```python
X[[0, 3, 5]]
```

---

# `np.where`

Get indices satisfying a condition:

```python
indices = np.where(score > 0.5)
```

Conditional replacement:

```python
result = np.where(score > 0.5, 1, 0)
```

Meaning:

```text
if condition:
    1
else:
    0
```

---

# `axis`

This is one of the most important NumPy concepts.

Given:

```python
X = np.array([
    [1, 2, 3],
    [4, 5, 6],
])
```

Shape:

```python
X.shape
# (2, 3)
```

Think:

```text
axis=0 -> collapse rows -> result per column
axis=1 -> collapse columns -> result per row
```

Column-wise mean:

```python
X.mean(axis=0)
```

Result:

```python
array([2.5, 3.5, 4.5])
```

Row-wise mean:

```python
X.mean(axis=1)
```

Result:

```python
array([2., 5.])
```

Mnemonic:

```text
axis=0 -> go down the rows
axis=1 -> go across the columns
```

---

# Aggregation

Common:

```python
np.sum(X)
np.mean(X)
np.std(X)
np.min(X)
np.max(X)
```

By column:

```python
X.mean(axis=0)
```

By row:

```python
X.mean(axis=1)
```

Keep dimensions:

```python
X.mean(axis=0, keepdims=True)
```

Without `keepdims`:

```text
(1, 3) -> (3,)
```

With `keepdims=True`:

```text
(1, 3)
```

This can help broadcasting.

---

# `reshape`

Change shape without changing data count.

```python
x = np.array([1, 2, 3, 4, 5, 6])
```

```python
x.reshape(2, 3)
```

Result:

```python
array([
    [1, 2, 3],
    [4, 5, 6],
])
```

`-1` means:

```text
infer this dimension automatically
```

Example:

```python
x.reshape(-1, 1)
```

Result shape:

```python
(6, 1)
```

Useful when a library expects a 2D feature matrix.

---

# `ravel` and `flatten`

Convert to 1D:

```python
X.ravel()
```

```python
X.flatten()
```

Difference:

```text
ravel()   often returns a view when possible
flatten() always returns a copy
```

---

# `squeeze`

Remove dimensions of size 1.

```python
x.shape
# (100, 1)
```

```python
x.squeeze().shape
# (100,)
```

Be careful: uncontrolled `squeeze()` can remove more dimensions than expected.

Specific axis:

```python
x.squeeze(axis=1)
```

---

# Add a Dimension

Using `np.newaxis`:

```python
x = np.array([1, 2, 3])
```

Column:

```python
x[:, np.newaxis]
# shape (3, 1)
```

Row:

```python
x[np.newaxis, :]
# shape (1, 3)
```

Equivalent:

```python
np.expand_dims(x, axis=1)
```

---

# Transpose

```python
X.T
```

Example:

```python
X.shape
# (2, 3)

X.T.shape
# (3, 2)
```

For a 1D array:

```python
x.shape
# (3,)

x.T.shape
# (3,)
```

A 1D vector has no row/column orientation, so `.T` changes nothing.

Use `reshape` or `np.newaxis` if you need `(1, 3)` or `(3, 1)`.

---

# `np.concatenate`

General-purpose concatenation along an existing axis.

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

Vertical:

```python
np.concatenate([A, B], axis=0)
```

Shape:

```text
(2, 2) + (2, 2) -> (4, 2)
```

Horizontal:

```python
np.concatenate([A, B], axis=1)
```

Shape:

```text
(2, 2) + (2, 2) -> (2, 4)
```

---

# `np.vstack`

Vertical stacking.

```python
np.vstack([A, B])
```

Conceptually:

```text
put B below A
```

---

# `np.hstack`

Horizontal stacking.

```python
np.hstack([A, B])
```

Conceptually:

```text
put B to the right of A
```

Example feature construction:

```python
feature_a = np.array([[0.1], [0.2], [0.3]])
feature_b = np.array([[10], [20], [30]])

X = np.hstack([feature_a, feature_b])
```

Result:

```python
array([
    [0.1, 10.0],
    [0.2, 20.0],
    [0.3, 30.0],
])
```

Shape:

```text
(3, 1) + (3, 1) -> (3, 2)
```

---

# `np.stack`

Unlike `concatenate`, `stack` creates a new axis.

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
```

```python
np.stack([a, b])
```

Shape:

```text
(3,) + (3,) -> (2, 3)
```

With:

```python
np.stack([a, b], axis=1)
```

Shape:

```text
(3, 2)
```

Rule:

```text
concatenate -> join along an existing axis
stack       -> create a new axis
```

---

# Quick Comparison: Stack Functions

```text
concatenate : general-purpose join
hstack      : join horizontally
vstack      : join vertically
stack       : create a new dimension
```

Always check:

```python
print(A.shape)
print(B.shape)
```

before stacking.

---

# Broadcasting

Broadcasting lets NumPy operate on arrays with compatible shapes.

Example:

```python
X = np.array([
    [1, 2, 3],
    [4, 5, 6],
])

mean = np.array([2.5, 3.5, 4.5])

X - mean
```

`mean` has shape:

```text
(3,)
```

`X` has shape:

```text
(2, 3)
```

NumPy conceptually applies the same `mean` row to every sample.

This is why:

```python
X_standardized = (X - mean) / std
```

works naturally.

---

# Broadcasting Rule

Compare dimensions from the right.

Dimensions are compatible when:

```text
same size
or
one of them is 1
```

Examples:

```text
(100, 5)
(5,)
```

compatible.

```text
(100, 5)
(1, 5)
```

compatible.

```text
(100, 5)
(100,)
```

usually not compatible as intended.

---

# Copies vs Views

Slicing often returns a view:

```python
x = np.array([1, 2, 3, 4])

part = x[:2]
part[0] = 999
```

`x` may also change.

If you need independence:

```python
part = x[:2].copy()
```

Use `.copy()` when mutating a sliced array and you do not want to modify the original.

---

# Sorting

Values:

```python
np.sort(scores)
```

Indices that would sort:

```python
np.argsort(scores)
```

Descending order:

```python
np.argsort(scores)[::-1]
```

Top 3 indices:

```python
top3 = np.argsort(scores)[::-1][:3]
```

---

# `argmax` / `argmin`

Index of maximum:

```python
np.argmax(scores)
```

Index of minimum:

```python
np.argmin(scores)
```

For matrices:

```python
np.argmax(X, axis=1)
```

returns the maximum column index for each row.

Common classification pattern:

```python
predicted_class = np.argmax(logits, axis=1)
```

---

# `np.unique`

Unique values:

```python
np.unique(y)
```

With counts:

```python
values, counts = np.unique(y, return_counts=True)
```

Useful for checking class balance.

---

# Random Numbers

Recommended modern API:

```python
rng = np.random.default_rng(42)
```

Random floats:

```python
rng.random(5)
```

Random integers:

```python
rng.integers(0, 10, size=5)
```

Shuffle:

```python
rng.shuffle(x)
```

Fixed seed improves reproducibility.

---

# Matrix Multiplication

Element-wise multiplication:

```python
A * B
```

Matrix multiplication:

```python
A @ B
```

or:

```python
np.matmul(A, B)
```

Dot product:

```python
np.dot(a, b)
```

For machine learning, pay close attention to shapes.

Example:

```text
X: (100, 5)
W: (5, 3)

X @ W -> (100, 3)
```

---

# A Common Linear Model Shape

```python
logits = X @ W + b
```

Typical shapes:

```text
X      : (N, D)
W      : (D, C)
b      : (C,)
logits : (N, C)
```

Where:

```text
N = number of samples
D = number of features
C = number of classes
```

---

# Pandas Basics

Create DataFrame:

```python
df = pd.DataFrame({
    "name": ["Alice", "Bob"],
    "score": [0.8, 0.9],
})
```

Inspect:

```python
df.head()
df.shape
df.columns
df.dtypes
df.info()
df.describe()
```

Select column:

```python
df["score"]
```

Select multiple columns:

```python
df[["name", "score"]]
```

Filter:

```python
df[df["score"] > 0.8]
```

Multiple conditions:

```python
df[(df["score"] > 0.8) & (df["name"] != "Alice")]
```

---

# `loc` vs `iloc`

Label-based:

```python
df.loc[0, "score"]
```

Position-based:

```python
df.iloc[0, 1]
```

Rule:

```text
loc  -> labels
iloc -> integer positions
```

---

# Missing Values

Check:

```python
df.isna().sum()
```

Drop rows:

```python
df.dropna()
```

Fill:

```python
df["score"] = df["score"].fillna(0)
```

Do not blindly fill missing values without considering what missingness means.

---

# Machine Learning Data Convention

Usually:

```text
X = input features
y = target / label
```

Example:

```python
X = np.array([
    [0.8, 10.0],
    [0.3,  2.0],
    [0.7,  8.0],
])

y = np.array([1, 0, 1])
```

Shapes:

```text
X.shape -> (3, 2)
y.shape -> (3,)
```

---

# Train / Validation / Test

Typical roles:

```text
train      -> fit model parameters
validation -> choose hyperparameters / compare models
test       -> final unbiased evaluation
```

For small experiments, train/test is common:

```python
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
)
```

For classification, often use:

```python
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y,
)
```

`stratify=y` approximately preserves class ratios.

---

# Standardization

Standardization transforms each feature independently.

Formula:

```text
z = (x - mean) / standard_deviation
```

Important:

```text
standardize feature-by-feature
not by mixing unrelated columns together
```

Example matrix:

```text
column 0 = feature A
column 1 = feature B
column 2 = feature C
```

Each column gets its own:

```text
mean
standard deviation
```

NumPy:

```python
mean = X_train.mean(axis=0)
std = X_train.std(axis=0)

X_train_std = (X_train - mean) / std
X_test_std = (X_test - mean) / std
```

Important:

```text
compute mean/std from training data only
```

---

# StandardScaler

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
```

Correct:

```text
train -> fit_transform
test  -> transform
```

Avoid:

```python
scaler.fit_transform(X_test)
```

because it lets test-set statistics influence preprocessing.

---

# Standardization vs Min-Max Scaling

Standardization:

```text
mean -> about 0
standard deviation -> about 1
```

Min-max scaling:

```text
typically maps values into [0, 1]
```

Example:

```python
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
```

Use based on model assumptions and feature characteristics.

---

# Standardization vs Vector Normalization

These are different.

Standardization:

```text
operate feature-by-feature across samples
```

Vector normalization:

```text
operate sample-by-sample, often forcing vector length to 1
```

L2 normalization:

```python
from sklearn.preprocessing import normalize

X_norm = normalize(X, norm="l2")
```

Common with vector similarity.

---

# Which Models Often Benefit from Scaling?

Scaling is commonly useful for:

```text
linear/logistic regression with regularization
SVM
k-nearest neighbors
k-means
neural networks
PCA
distance-based methods
```

Tree-based models often need it less:

```text
decision tree
random forest
gradient-boosted trees
```

Reason:

```text
distance and gradient-based models are sensitive to feature scale
tree splits mostly depend on ordering / thresholds
```

---

# Binary / Categorical Features

A binary feature:

```text
0 / 1
```

does not always need standardization.

Example:

```text
continuous feature A
continuous feature B
binary flag
```

It is common to scale the continuous features while leaving the binary flag unchanged.

Whether to scale depends on the model and experiment design.

---

# Data Leakage

Data leakage means information unavailable at prediction time leaks into training.

Common mistake:

```python
scaler.fit(X)
X_scaled = scaler.transform(X)

X_train, X_test, ... = train_test_split(X_scaled, ...)
```

Problem:

```text
the scaler saw the test data
```

Better:

```python
X_train, X_test, y_train, y_test = train_test_split(...)

scaler.fit(X_train)

X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)
```

General rule:

```text
split first
fit preprocessing on train only
apply the learned preprocessing to validation/test
```

---

# Pipeline

Pipelines reduce leakage mistakes.

Example:

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

The scaler is fitted only inside training.

---

# Baseline First

Before adding complicated features or models, establish a baseline.

Example:

```text
baseline model
    ↓
evaluate
    ↓
change one thing
    ↓
evaluate again
```

Avoid changing many things at once.

Otherwise you cannot tell which change helped.

---

# `fit`, `transform`, `predict`

Common scikit-learn vocabulary:

```text
fit       -> learn parameters from data
transform -> apply learned transformation
predict   -> produce predictions
```

Examples:

```python
scaler.fit(X_train)
X_scaled = scaler.transform(X_train)
```

```python
model.fit(X_train, y_train)
pred = model.predict(X_test)
```

---

# `fit_transform`

Shortcut for:

```python
transformer.fit(X)
transformer.transform(X)
```

Equivalent:

```python
X2 = transformer.fit_transform(X)
```

Use mainly on training data.

---

# Classification Probabilities

Some classifiers provide:

```python
proba = model.predict_proba(X_test)
```

Typical shape:

```text
(N, C)
```

For binary classification:

```python
positive_probability = proba[:, 1]
```

---

# Accuracy

```python
accuracy_score(y_true, y_pred)
```

Formula:

```text
correct predictions / all predictions
```

Accuracy can be misleading when classes are highly imbalanced.

---

# Precision

```text
Among predicted positives,
how many were actually positive?
```

Formula:

```text
TP / (TP + FP)
```

Useful when false positives are costly.

---

# Recall

```text
Among actual positives,
how many did we find?
```

Formula:

```text
TP / (TP + FN)
```

Useful when missing positives is costly.

---

# F1 Score

Harmonic mean of precision and recall:

```text
F1 = 2 * precision * recall / (precision + recall)
```

Useful when both precision and recall matter.

---

# Metrics in scikit-learn

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

Binary classification layout:

```text
[[TN, FP],
 [FN, TP]]
```

Useful when a single metric hides the type of mistake being made.

---

# Class Imbalance

Check counts:

```python
np.unique(y, return_counts=True)
```

or:

```python
pd.Series(y).value_counts()
```

If one class dominates, accuracy may look good even with a poor model.

Consider:

```text
precision
recall
F1
confusion matrix
stratified split
class weights
```

---

# Reproducibility

Use fixed random seeds where possible.

Example:

```python
random_state=42
```

NumPy:

```python
rng = np.random.default_rng(42)
```

Reproducibility matters when comparing experiments.

---

# Overfitting

Typical pattern:

```text
training performance   very high
validation performance much lower
```

Possible causes:

```text
model too complex
too little data
too many features
data leakage
too many training epochs
```

Always compare training and validation/test performance.

---

# Underfitting

Typical pattern:

```text
training performance   poor
validation performance poor
```

Possible causes:

```text
model too simple
features insufficient
training insufficient
strong regularization
```

---

# Feature Engineering

A feature is a measurable input used by the model.

Examples:

```text
length
count
similarity score
binary flag
frequency
category
```

Useful practice:

```text
one row    = one sample
one column = one feature
```

Do not add features just because they are available.

Ask:

```text
Does this feature contain useful information at prediction time?
```

---

# Feature Scale

Suppose:

```text
feature A: 0.0 to 1.0
feature B: 0 to 10000
```

A scale-sensitive model may be dominated by feature B simply because its numeric magnitude is much larger.

Standardization can reduce this problem.

---

# Cosine Similarity

For vectors `a` and `b`:

```text
cosine_similarity =
(a · b) / (||a|| ||b||)
```

Using NumPy:

```python
cos_sim = np.dot(a, b) / (
    np.linalg.norm(a) * np.linalg.norm(b)
)
```

For already L2-normalized vectors:

```text
cosine similarity = dot product
```

---

# Euclidean Distance

```python
distance = np.linalg.norm(a - b)
```

Smaller means closer.

Cosine similarity focuses more on direction than vector magnitude.

---

# Softmax

Converts logits into probabilities-like values that sum to 1.

Stable implementation:

```python
def softmax(x):
    x = x - np.max(x, axis=-1, keepdims=True)
    exp_x = np.exp(x)
    return exp_x / np.sum(exp_x, axis=-1, keepdims=True)
```

Subtracting the maximum improves numerical stability.

---

# Logits

Logits are raw model scores before softmax.

Example:

```python
logits = np.array([2.0, 0.5, -1.0])
```

They are not probabilities.

After softmax:

```python
probs = softmax(logits)
```

Now:

```python
probs.sum()
# approximately 1.0
```

---

# Cross Entropy

For a correct class `y`:

```text
loss = -log(probability assigned to the correct class)
```

If the model gives the correct class high probability:

```text
loss -> small
```

If the model gives the correct class low probability:

```text
loss -> large
```

---

# Margin Ranking Intuition

A ranking objective may try to enforce:

```text
positive_score > negative_score + margin
```

One common form:

```text
loss = max(0, margin - positive_score + negative_score)
```

If the positive is already sufficiently above the negative:

```text
loss = 0
```

---

# Hard Negatives

A hard negative is:

```text
an incorrect example that looks similar to a correct example
```

Easy negative:

```text
obviously unrelated
```

Hard negative:

```text
similar wording / similar features / similar context
but still incorrect
```

Hard negatives can provide stronger training signals, but overly noisy negatives can hurt training.

---

# Nearest-Neighbor Top-K Pattern

Given similarity scores:

```python
scores = np.array([0.3, 0.9, 0.6, 0.8])
```

Top K indices:

```python
k = 2
top_k = np.argsort(scores)[::-1][:k]
```

Result:

```text
indices of the 2 largest scores
```

Retrieve:

```python
top_scores = scores[top_k]
```

---

# Common Shape Pattern: Features

Suppose:

```python
feature_a.shape
# (100,)

feature_b.shape
# (100,)
```

Direct:

```python
np.hstack([feature_a, feature_b])
```

gives:

```text
(200,)
```

which is often not what you want.

Convert each to columns:

```python
feature_a = feature_a.reshape(-1, 1)
feature_b = feature_b.reshape(-1, 1)

X = np.hstack([feature_a, feature_b])
```

Now:

```text
X.shape == (100, 2)
```

This is a very common ML pattern.

---

# Common Shape Pattern: Labels

Libraries often expect:

```text
X: (N, D)
y: (N,)
```

Not:

```text
y: (N, 1)
```

If necessary:

```python
y = y.ravel()
```

---

# Common Shape Pattern: One Sample

Suppose one sample is:

```python
x = np.array([0.5, 1.2, 3.0])
```

Shape:

```text
(3,)
```

Many scikit-learn models expect:

```text
(number_of_samples, number_of_features)
```

So:

```python
x = x.reshape(1, -1)
```

Shape:

```text
(1, 3)
```

Then:

```python
model.predict(x)
```

---

# Common Shape Pattern: One Feature

Suppose:

```python
x = np.array([10, 20, 30, 40])
```

and these are 4 samples of one feature.

Use:

```python
X = x.reshape(-1, 1)
```

Shape:

```text
(4, 1)
```

---

# Common Error: Inconsistent Sample Counts

Bad:

```text
X.shape = (100, 5)
y.shape = (99,)
```

The number of samples must match:

```text
X.shape[0] == y.shape[0]
```

Quick assertion:

```python
assert X.shape[0] == y.shape[0]
```

---

# Assertions

Useful for catching bugs early.

```python
assert X.ndim == 2
assert y.ndim == 1
assert X.shape[0] == y.shape[0]
```

Check finite values:

```python
assert np.isfinite(X).all()
```

---

# NaN / Infinity

Check NaN:

```python
np.isnan(X).any()
```

Check finite:

```python
np.isfinite(X).all()
```

Count NaN:

```python
np.isnan(X).sum()
```

NaNs can silently break optimization and metrics.

---

# Safe Division

Potential issue:

```python
x / std
```

if `std == 0`.

Example protection:

```python
std = np.where(std == 0, 1, std)
```

A feature with zero standard deviation is constant and often not useful.

---

# Logging Shapes During Development

A useful debugging pattern:

```python
print("X:", X.shape)
print("y:", y.shape)
print("W:", W.shape)
print("logits:", logits.shape)
```

Shape bugs are easier to fix close to where they occur.

---

# Useful Python Built-ins

```python
len(x)
sum(x)
min(x)
max(x)
sorted(x)
any(x)
all(x)
```

Example:

```python
any(score > 0.8 for score in scores)
```

---

# `sorted` vs `.sort()`

Return a new list:

```python
new_values = sorted(values)
```

Modify list in place:

```python
values.sort()
```

Descending:

```python
sorted(values, reverse=True)
```

---

# Dictionary Sorting

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

# `map` and `filter`

Possible:

```python
result = list(map(lambda x: x * 2, values))
```

But list comprehensions are often more readable:

```python
result = [x * 2 for x in values]
```

Filter:

```python
positive = [x for x in values if x > 0]
```

---

# Unpacking

```python
a, b = [10, 20]
```

Ignore value:

```python
a, _ = [10, 20]
```

Extended unpacking:

```python
first, *middle, last = [1, 2, 3, 4, 5]
```

---

# `*args`

Variable positional arguments:

```python
def add_all(*values):
    return sum(values)
```

```python
add_all(1, 2, 3)
```

---

# `**kwargs`

Variable keyword arguments:

```python
def show(**kwargs):
    print(kwargs)
```

```python
show(name="Alice", score=0.9)
```

---

# Dataclasses

Useful for structured configuration or records.

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

# Type Hints for NumPy

Basic Python:

```python
def normalize(values: np.ndarray) -> np.ndarray:
    ...
```

For larger projects, stronger typing can improve readability and editor support.

---

# Useful scikit-learn Pattern

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

For production-style experiments, prefer a `Pipeline`.

---

# Better scikit-learn Pattern: Pipeline

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

Benefits:

```text
less preprocessing boilerplate
lower leakage risk
easier cross-validation
easier deployment
```

---

# Cross Validation

Basic example:

```python
from sklearn.model_selection import cross_val_score

scores = cross_val_score(
    model,
    X,
    y,
    cv=5,
)
```

Use cross-validation when a single train/test split is too unstable.

Do not use the final test set repeatedly for model selection.

---

# Thresholds

Binary classifiers often use a probability threshold such as:

```text
0.5
```

But the best threshold depends on the cost of:

```text
false positives
false negatives
```

Example:

```python
proba = model.predict_proba(X_test)[:, 1]

pred = (proba >= 0.7).astype(int)
```

Changing the threshold changes precision/recall trade-offs.

---

# Debugging Model Performance

When performance is poor, ask in this order:

```text
1. Are labels correct?
2. Are train/test splits correct?
3. Is there leakage?
4. Are shapes correct?
5. Are features meaningful?
6. Are classes imbalanced?
7. Is preprocessing appropriate?
8. Is the baseline already strong?
9. Is the model overfitting?
10. Does the metric match the real objective?
```

---

# Practical Experiment Rule

Change one major variable at a time.

Good:

```text
baseline
    ↓
add standardization
    ↓
compare
    ↓
add one feature
    ↓
compare
```

Hard to interpret:

```text
change model
change features
change preprocessing
change loss
change threshold
all at once
```

---

# Common NumPy Mistakes

## Mistake 1: Confusing `(N,)` and `(N, 1)`

```python
x.shape
# (100,)
```

vs:

```python
x.reshape(-1, 1).shape
# (100, 1)
```

---

## Mistake 2: Wrong `axis`

Check:

```python
X.shape
```

then ask:

```text
Do I want one result per column?
-> axis=0

Do I want one result per row?
-> axis=1
```

---

## Mistake 3: Using Python `and` on NumPy arrays

Wrong:

```python
(a > 0) and (a < 1)
```

Correct:

```python
(a > 0) & (a < 1)
```

---

## Mistake 4: Forgetting Parentheses Around Conditions

Prefer:

```python
(a > 0) & (a < 1)
```

not:

```python
a > 0 & a < 1
```

Operator precedence can produce unexpected behavior.

---

## Mistake 5: Accidentally Flattening Features

Bad:

```python
np.hstack([feature_a, feature_b])
```

when both are `(N,)`.

Often intended:

```python
np.column_stack([feature_a, feature_b])
```

or:

```python
np.hstack([
    feature_a.reshape(-1, 1),
    feature_b.reshape(-1, 1),
])
```

---

# `np.column_stack`

Convenient for converting 1D feature arrays into columns.

```python
a = np.array([1, 2, 3])
b = np.array([10, 20, 30])

X = np.column_stack([a, b])
```

Result:

```python
array([
    [1, 10],
    [2, 20],
    [3, 30],
])
```

Shape:

```text
(3, 2)
```

Often cleaner than manual reshape + hstack.

---

# Useful Shape Mental Model

Given:

```text
X.shape = (N, D)
```

Think:

```text
N = how many examples?
D = how many values describe each example?
```

Given:

```text
logits.shape = (N, C)
```

Think:

```text
N = how many examples?
C = how many class scores per example?
```

This mental model makes many ML expressions easier to read.

---

# Final Practical Checklist

Before training:

```text
[ ] X and y sample counts match
[ ] train/test split done before fitting preprocessing
[ ] class balance checked
[ ] NaN / inf checked
[ ] feature meanings understood
[ ] baseline recorded
```

During implementation:

```text
[ ] print shape at important steps
[ ] distinguish (N,) from (N,1)
[ ] verify axis=0 vs axis=1
[ ] use parentheses in boolean masks
[ ] check stack/concatenate output shape
```

During evaluation:

```text
[ ] choose metrics that match the objective
[ ] compare against baseline
[ ] inspect confusion matrix when relevant
[ ] avoid tuning repeatedly on the final test set
[ ] change one major thing at a time
```

---

# Very Short Reference

```python
# first N elements
x[:N]

# from N onward
x[N:]

# boolean filter
x[condition]

# multiple conditions
x[(a > 0) & (a < 1)]

# first column
X[:, 0]

# first 3 rows
X[:3, :]

# shape
X.shape

# reshape into one column
x.reshape(-1, 1)

# reshape one sample
x.reshape(1, -1)

# column-wise mean
X.mean(axis=0)

# row-wise mean
X.mean(axis=1)

# horizontal feature combination
np.column_stack([a, b])

# vertical stack
np.vstack([A, B])

# horizontal stack
np.hstack([A, B])

# new axis
np.stack([a, b])

# top-k descending
idx = np.argsort(scores)[::-1][:k]

# maximum index
idx = np.argmax(scores)

# unique values + counts
np.unique(y, return_counts=True)

# matrix multiplication
X @ W

# standardization
X_scaled = (X - mean) / std
```
