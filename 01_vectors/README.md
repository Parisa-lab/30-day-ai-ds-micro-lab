# Vectors

**AI/DS Micro-Lab — Day 01**

A first step into linear algebra for AI and Data Science.

---

## 1. What Is a Vector?

A **vector** is an ordered collection of numbers.

A vector can be written as a column:

```text
x =
[  3 ]
[ 50 ]
[  9 ]
```

In Python:

```python
x = [3, 50, 9]
```

Each number is a **component** of the vector.

---

## 2. Components

For:

```python
x = [3, 50, 9]
```

the components are:

| Index | Component |
|------:|----------:|
| `0` | `3` |
| `1` | `50` |
| `2` | `9` |

Python uses **zero-based indexing**.

```python
x[0]   # 3
x[1]   # 50
x[2]   # 9
x[-1]  # 9
```

`x[-1]` accesses the **last component**.

---

## 3. Dimension

The **dimension of a vector** is the number of components it contains.

Example:

```python
x = [4, 7, 2, 9]
```

This vector contains four components.

Therefore:

```text
dimension(x) = 4
```

In Python:

```python
len(x)
```

returns:

```text
4
```

### Important

Changing a component does not change the dimension.

```python
x = [3, 50, 9]

x[1] = 100
```

The result is:

```text
[3, 100, 9]
```

The dimension is still:

```text
3
```

---

## 4. Vector Addition

Vectors are added **component by component**.

Consider:

```text
a =       b =

[ 3 ]     [ 1 ]
[50 ]     [ 2 ]
[ 9 ]     [ 4 ]
```

Add the corresponding components:

```text
3  + 1  =  4
50 + 2  = 52
9  + 4  = 13
```

Therefore:

```text
a + b =

[  4 ]
[ 52 ]
[ 13 ]
```

In Python:

```python
a = [3, 50, 9]
b = [1, 2, 4]
```

The result is:

```text
[4, 52, 13]
```

---

## 5. Dimension Compatibility

Two vectors can be added only when they have the **same dimension**.

### Valid addition

```python
a = [3, 50, 9]
b = [1, 2, 4]
```

Their dimensions are:

```text
dimension(a) = 3
dimension(b) = 3
```

Therefore, addition is defined.

### Invalid addition

```python
a = [1, 2, 3]
b = [4, 5]
```

Their dimensions are:

```text
dimension(a) = 3
dimension(b) = 2
```

Since:

```text
3 != 2
```

the vectors cannot be added.

### Fundamental Rule

> **Vector addition requires equal dimensions.**

---

## 6. Python Lists vs. Mathematical Vectors

A Python list is not automatically treated as a mathematical vector.

For example:

```python
[1, 2, 3] + [4, 5, 6]
```

produces:

```text
[1, 2, 3, 4, 5, 6]
```

This is called **list concatenation**.

Python joins the two lists together.

It does **not** calculate:

```text
[1 + 4, 2 + 5, 3 + 6]
```

Therefore, mathematical vector addition must be implemented explicitly.

---

## 7. Implementing Vector Addition

The function in `vector.py` is:

```python
def vector_add(a, b):
    if len(a) == len(b):
        return [a[i] + b[i] for i in range(len(a))]
    else:
        raise ValueError("Vectors must have the same dimension.")
```

### Step 1 — Check the dimensions

```python
len(a) == len(b)
```

If this is `True`, the vectors have the same dimension.

### Step 2 — Add corresponding components

```python
[a[i] + b[i] for i in range(len(a))]
```

For example:

```text
a = [3, 50, 9]
b = [1, 2, 4]

a[0] + b[0] = 3  + 1 = 4
a[1] + b[1] = 50 + 2 = 52
a[2] + b[2] = 9  + 4 = 13
```

Result:

```text
[4, 52, 13]
```

### Step 3 — Reject incompatible vectors

If the dimensions are different:

```python
raise ValueError("Vectors must have the same dimension.")
```

Python stops the operation and reports the problem.

---

## 8. Why `ValueError`?

Consider:

```python
a = [1, 2, 3]
b = [4, 5]
```

The dimensions are different:

```text
dimension(a) = 3
dimension(b) = 2
```

Therefore, vector addition is not defined.

Instead of silently producing an incorrect result, the function raises:

```text
ValueError: Vectors must have the same dimension.
```

This makes the invalid input explicit.

---

## 9. Vectors in AI and Data Science

Vectors are fundamental to AI and Data Science.

A data point can be represented as a vector of features.

For example:

```text
x =
[ age        ]
[ income     ]
[ experience ]
```

A specific data point might be:

```python
x = [35, 60000, 8]
```

This means:

```text
age        = 35
income     = 60000
experience = 8
```

The vector has dimension:

```text
3
```

Vectors will later be used to represent:

- Features
- Data points
- Model parameters
- Embeddings
- Neural-network activations
- Optimization variables

---

## 10. What We Learned

| Concept | Meaning |
|---|---|
| Vector | An ordered collection of numbers |
| Component | An individual number in a vector |
| Dimension | Number of components |
| Index | Position of a component |
| Zero-based indexing | Python starts indexing at `0` |
| `x[-1]` | Last component |
| Mutable list | A list whose components can be changed |
| Vector addition | Addition of corresponding components |
| Dimension compatibility | Vectors must have equal dimensions |
| List concatenation | Python's behavior for `list + list` |
| `ValueError` | Used to reject incompatible vectors |

---

## 11. Fundamental Rule

```text
Vector addition
       |
       v
Do the dimensions match?
       |
   +---+---+
   |       |
  YES      NO
   |       |
   v       v
 Add     Reject
components
```

> **Before adding two vectors, check that their dimensions are equal.**

---

## 12. Project Structure

```text
30-day-ai-ds-micro-lab/
└── 01_vectors/
    ├── README.md
    └── vector.py
```

`vector.py` contains the Python implementation developed during this lesson.