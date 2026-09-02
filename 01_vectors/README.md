# Vectors

**AI/DS Micro-Lab — Day 01**

A first step into linear algebra for AI and Data Science.

---

## 1. What Is a Vector?

A **vector** is an ordered collection of numbers.

$$
\mathbf{x} =
\begin{bmatrix}
3 \\
50 \\
9
\end{bmatrix}
$$

In Python:

    x = [3, 50, 9]

Each number is a **component** of the vector.

---

## 2. Dimension

The **dimension of a vector** is the number of components it contains.

    x = [4, 7, 2, 9]

Therefore:

$$
\dim(\mathbf{x}) = 4
$$

In Python:

    len(x)

returns:

    4

---

## 3. Accessing Components

Python uses **zero-based indexing**.

    x = [3, 50, 9]

    x[0]   # 3
    x[1]   # 50
    x[2]   # 9
    x[-1]  # 9

---

## 4. Changing a Component

Python lists are mutable, so we can change a component.

    x = [3, 50, 9]

    x[1] = 100

The vector becomes:

    [3, 100, 9]

Its dimension is still **3**.

---

## 5. Vector Addition

Vectors are added **component by component**.

$$
\mathbf{a} =
\begin{bmatrix}
3 \\
50 \\
9
\end{bmatrix}
\qquad
\mathbf{b} =
\begin{bmatrix}
1 \\
2 \\
4
\end{bmatrix}
$$

$$
\mathbf{a} + \mathbf{b}
=
\begin{bmatrix}
3 + 1 \\
50 + 2 \\
9 + 4
\end{bmatrix}
=
\begin{bmatrix}
4 \\
52 \\
13
\end{bmatrix}
$$

### Important Rule

Two vectors can be added only if they have the **same dimension**.

$$
\boxed{\dim(\mathbf{a}) = \dim(\mathbf{b})}
$$

For example:

    a = [1, 2, 3]
    b = [4, 5]

Here:

$$
\dim(\mathbf{a}) = 3
$$

$$
\dim(\mathbf{b}) = 2
$$

Since:

$$
3 \ne 2
$$

the vectors cannot be added.

---

## 6. Python Lists vs. Mathematical Vectors

Python's `+` operator does **not** perform mathematical vector addition on lists.

    [1, 2, 3] + [4, 5, 6]

produces:

    [1, 2, 3, 4, 5, 6]

This is **list concatenation**.

Mathematical vector addition must be implemented component by component.

---

## 7. Implementation

    def vector_add(a, b):
        if len(a) == len(b):
            return [a[i] + b[i] for i in range(len(a))]
        else:
            raise ValueError("Vectors must have the same dimension.")

The function:

1. Checks whether the dimensions match.
2. Adds corresponding components.
3. Raises `ValueError` when the dimensions are different.

---

## 8. Why `ValueError`?

Suppose:

    a = [1, 2, 3]
    b = [4, 5]

The dimensions are:

$$
\dim(\mathbf{a}) = 3
$$

$$
\dim(\mathbf{b}) = 2
$$

Because:

$$
3 \ne 2
$$

vector addition is not defined.

The function therefore raises:

    ValueError: Vectors must have the same dimension.

This prevents the program from silently performing an invalid operation.

---

## 9. Vectors in AI and Data Science

Vectors are fundamental to AI and Data Science.

A data point can be represented as a vector of features:

$$
\mathbf{x} =
\begin{bmatrix}
\text{age} \\
\text{income} \\
\text{experience}
\end{bmatrix}
$$

For example:

    x = [35, 60000, 8]

This vector has dimension **3**.

Vectors will later be used for:

- Machine-learning features
- Model parameters
- Embeddings
- Neural networks
- Optimization
- Matrix operations

---

## 10. Key Takeaways

- **Vector:** An ordered collection of numbers.
- **Component:** An individual number in a vector.
- **Dimension:** The number of components.
- **Python indexing:** Starts at `0`.
- **`x[-1]`:** Accesses the last component.
- **Vector addition:** Add corresponding components.
- **Addition requirement:** Dimensions must be equal.
- **Python list `+`:** Concatenates lists.
- **`ValueError`:** Rejects vectors with incompatible dimensions.

The fundamental rule:

$$
\boxed{\text{Vector addition requires equal dimensions.}}
$$

---

## Project Structure

    30-day-ai-ds-micro-lab/
    └── 01_vectors/
        ├── README.md
        └── vector.py