---

# 📦 Python `collections` Module – Revision Notes

The `collections` module provides **specialized container datatypes** that extend Python’s built-in data structures like `list`, `dict`, `set`, and `tuple`.

```python
import collections
# or
from collections import *
```

---

## 1️⃣ `Counter`

👉 Used to **count hashable objects** (like frequency maps)

### 🔹 Key Features

* Counts elements in iterable
* Returns a dictionary-like object
* Supports math operations

### 📌 Example

```python
from collections import Counter

data = ["a", "b", "a", "c", "b", "a"]
count = Counter(data)

print(count)
# Counter({'a': 3, 'b': 2, 'c': 1})
```

### 📌 Common Operations

```python
count.most_common(2)   # [('a', 3), ('b', 2)]
count['a']             # 3
count.update(['a','b'])
```

### 🔥 Use Cases

* Word frequency (NLP)
* Log analysis
* Vote counting

---

## 2️⃣ `defaultdict`

👉 Dictionary with a **default value** for missing keys

### 🔹 Why?

Avoids `KeyError` and manual initialization.

### 📌 Example

```python
from collections import defaultdict

d = defaultdict(int)
d['a'] += 1

print(d)  # {'a': 1}
```

### 📌 Other Defaults

```python
defaultdict(list)
defaultdict(set)
defaultdict(dict)
```

### 🔥 Use Cases

* Grouping data
* Graph adjacency lists
* Counting without checks

---

## 3️⃣ `OrderedDict` (⚠️ Mostly historical)

👉 Dictionary that **preserves insertion order**

⚠️ **Note**: Since Python 3.7+, normal `dict` preserves order.

### 📌 Example

```python
from collections import OrderedDict

od = OrderedDict()
od['a'] = 1
od['b'] = 2
```

### 📌 Special Feature

```python
od.move_to_end('a')
```

### 🔥 Use Cases

* LRU Cache (older Python)
* Explicit order-sensitive logic

---

## 4️⃣ `namedtuple`

👉 Tuple with **named fields** (lightweight class)

### 📌 Example

```python
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
p = Point(10, 20)

print(p.x, p.y)
```

### 🔹 Benefits

* Immutable
* Faster than classes
* Self-documenting

### 🔥 Use Cases

* Coordinates
* Database rows
* Config objects

---

## 5️⃣ `deque`

👉 **Double-ended queue** (fast append & pop)

### 🔹 Why `deque`?

* O(1) append/pop from both ends
* Faster than list for queues

### 📌 Example

```python
from collections import deque

dq = deque([1, 2, 3])
dq.append(4)
dq.appendleft(0)

print(dq)
# deque([0, 1, 2, 3, 4])
```

### 📌 Useful Methods

```python
dq.pop()
dq.popleft()
dq.rotate(1)
```

### 🔥 Use Cases

* Queue / Stack
* Sliding window
* BFS in graphs

---

## 6️⃣ `ChainMap`

👉 Treat **multiple dictionaries as one**

### 📌 Example

```python
from collections import ChainMap

dict1 = {'a': 1}
dict2 = {'b': 2}

cm = ChainMap(dict1, dict2)
print(cm['b'])  # 2
```

### 🔹 Behavior

* Searches dictionaries left → right
* No merging (views only)

### 🔥 Use Cases

* Config layers
* Environment variables
* Scope resolution

---

## 7️⃣ `UserDict`, `UserList`, `UserString`

👉 Custom versions of built-in types

### 📌 Example

```python
from collections import UserDict

class MyDict(UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(key, value * 2)

d = MyDict()
d['a'] = 5
print(d)  # {'a': 10}
```

### 🔥 Use Cases

* Validation logic
* Logging access
* Controlled mutations

---

## ⚡ Quick Comparison Table

| Type        | Best For                                   |
| ----------- | ------------------------------------------ |
| Counter     | Frequency counting                         |
| defaultdict | Auto-init values flexible & programmable   |
| deque       | Fast queue/stack                           |
| namedtuple  | Lightweight objects                        |
| ChainMap    | Layered configs                            |
| UserDict    | Custom dict behavior                       |

---

## 🧠 Interview Tips

* Use `deque` instead of list for queues
* Use `Counter` instead of manual counting
* Prefer `defaultdict` for grouping
* Mention Python 3.7+ dict ordering

---

## 📌 One-Liner Summary

> `collections` gives you **faster, cleaner, and more expressive data structures** than basic Python types.

---