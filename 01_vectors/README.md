# Vector Fundamentals

This lesson introduces the basic idea of vectors and implements simple vector operations in Python.

The goal is to understand the mathematical concept first and then translate it into Python.

---

## 1. What Is a Vector?

A vector is an **ordered collection of numbers**.

For example:

```text
x = [3, 50, 9]
```

The numbers inside the vector are called **components**.

For this vector:

- `3` is the first component
- `50` is the second component
- `9` is the third component

In Python:

```python
x = [3, 50, 9]
```

---

## 2. Vector Components

Each number in a vector is called a **component**.

For:

```text
x = [3, 50, 9]
```

we have:

```text
First component  = 3
Second component = 50
Third component  = 9
```

Python uses **zero-based indexing**, so:

```python
x[0]  # 3
x[1]  # 50
x[2]  # 9
```

The relationship is:

```text
Python index:   0    1    2
                ↓    ↓    ↓
Vector:        [3,  50,   9]
```

---

## 3. Vector Dimension

The **dimension** of a vector is the number of components it contains.

For example:

```text
x = [3, 50, 9]
```

There are 3 components, so:

```text
dimension of x = 3
```

Another example:

```text
y = [4, 7, 2, 9]
```

This vector has 4 components, so its dimension is 4.

In Python:

```python
len(x)
```

returns the number of components.

---

## 4. Changing a Component

A vector's components can be changed.

For example:

```python
x = [7, 12, 5, 20]

x[2] = 100
```

The vector becomes:

```text
Before: [7, 12, 5, 20]
After:  [7, 12, 100, 20]
```

The third component changed because Python uses index `2` for the third position.

---

## 5. Vector Addition

Two vectors can be added **component by component**.

For example:

```text
a = [2, 3]
b = [4, 5]
```

Add corresponding components:

```text
2 + 4 = 6
3 + 5 = 8
```

Therefore:

```text
a + b = [6, 8]
```

The rule is:

```text
first component  + first component
second component + second component
third component  + third component
...
```

---

## 6. Vectors Must Have the Same Dimension

Vector addition is defined only when the two vectors have the **same dimension**.

For example:

```text
a = [1, 2, 3]
b = [4, 5, 6]
```

Both vectors have dimension 3, so they can be added:

```text
a + b = [5, 7, 9]
```

But:

```text
a = [1, 2, 3]
b = [4, 5]
```

cannot be added.

Their dimensions are different:

```text
dimension of a = 3
dimension of b = 2
```

There is no corresponding component in `b` for the third component of `a`.

Therefore:

**Vector addition is not defined for these two vectors.**

---

## 7. Python Lists Are Not Mathematical Vectors

Python's `+` operator for lists does **not** perform mathematical vector addition.

For example:

```python
a = [3, 7, 2]
b = [5, 1, 4]

print(a + b)
```

Python produces:

```text
[3, 7, 2, 5, 1, 4]
```

This is **list concatenation**, not vector addition.

Mathematical vector addition should produce:

```text
[8, 8, 6]
```

Therefore, we need to implement vector addition ourselves.

---

## 8. Implementing Vector Addition

We can add corresponding components using a loop:

```python
a = [3, 7, 2]
b = [5, 1, 4]

result = []

for i in range(len(a)):
    result.append(a[i] + b[i])

print(result)
```

Output:

```text
[8, 8, 6]
```

The loop performs:

```text
i = 0 → 3 + 5 = 8
i = 1 → 7 + 1 = 8
i = 2 → 2 + 4 = 6
```

---

## 9. List Comprehension

The same operation can be written more compactly using a list comprehension:

```python
[a[i] + b[i] for i in range(len(a))]
```

This means:

```text
For each index i:
    calculate a[i] + b[i]
    and put the result into a new list.
```

For example:

```python
a = [3, 7, 2]
b = [5, 1, 4]

result = [a[i] + b[i] for i in range(len(a))]
```

Result:

```text
[8, 8, 6]
```

---

## 10. The vector_add() Function

We can turn the operation into a reusable function:

```python
def vector_add(a, b):
    if len(a) == len(b):
        return [a[i] + b[i] for i in range(len(a))]
    else:
        raise ValueError("Vectors must have the same dimension.")
```

Example:

```python
a = [3, 50, 9]
b = [1, 2, 4]

print(vector_add(a, b))
```

Output:

```text
[4, 52, 13]
```

---

## 11. Why Use ValueError?

Suppose we try:

```python
a = [1, 2, 3]
b = [4, 5]

vector_add(a, b)
```

The dimensions are different, so vector addition is not defined.

The function raises:

```text
ValueError: Vectors must have the same dimension.
```

This is better than silently returning an incorrect result.

The function therefore enforces an important mathematical rule:

```text
If dimensions are equal:
    perform vector addition

If dimensions are different:
    raise an error
```

---

## 12. Vectors in AI and Data Science

Vectors are fundamental to AI and Data Science because we often represent an object using a collection of numerical features.

For example, suppose we describe a house using:

```text
x = [120, 3, 2]
```

where:

```text
120 = area
3   = number of bedrooms
2   = number of bathrooms
```

This is a vector with:

```text
3 components
dimension = 3
```

A machine learning model can use this vector as numerical input.

In general:

```text
x = [feature_1, feature_2, feature_3, ..., feature_n]
```

Vectors will later appear throughout:

- Machine Learning
- Linear Algebra
- Neural Networks
- Optimization
- Deep Learning
- Data Representation
- Embeddings

---

## 13. Key Takeaways

### Vector

A vector is an ordered collection of numbers.

```text
x = [3, 50, 9]
```

### Component

Each number inside a vector is a component.

```text
x = [3, 50, 9]
```

### Dimension

The number of components is the vector's dimension.

```text
x = [3, 50, 9]

dimension = 3
```

### Vector Addition

Vectors are added component by component.

```text
[2, 3] + [4, 5] = [6, 8]
```

### Dimension Compatibility

Vectors must have the same dimension to be added.

```text
[1, 2, 3] + [4, 5]
```

is not defined.

### Python

Python lists do not automatically perform mathematical vector addition.

```python
[1, 2] + [3, 4]
```

produces:

```text
[1, 2, 3, 4]
```

Therefore, we implement vector addition ourselves.

---

## Project Structure

```text
30-day-ai-ds-micro-lab/
│
└── 01_vectors/
    ├── vector.py
    └── README.md
```

The `vector.py` file contains the Python implementation for the concepts introduced in this lesson.

---

## Learning Pattern

This project follows a simple cycle:

```text
Learn one concept
       ↓
Code it from scratch
       ↓
Run the code
       ↓
Check the result
       ↓
Explain what happened
       ↓
Commit the work
```

The purpose is not just to make the code work.

The goal is to understand **why it works mathematically and how that mathematics is translated into Python**.
