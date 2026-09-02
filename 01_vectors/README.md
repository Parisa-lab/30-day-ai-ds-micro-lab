01 — Vectors

Part of the 30-Day AI/DS Micro-Lab

«Goal: Build a solid mathematical and Python foundation for AI and Data Science through small, executable experiments.»

---

What is a Vector?

A vector is an ordered collection of numbers.

Mathematically:

[
\mathbf{x} =
\begin{bmatrix}
3\
50\
9
\end{bmatrix}
]

In Python:

x = [3, 50, 9]

This vector has 3 components, so its dimension is:

[
\boxed{\dim(\mathbf{x}) = 3}
]

---

1. Vector Components

Each number in a vector is a component.

x = [3, 50, 9]

Index| Component
"0"| "3"
"1"| "50"
"2"| "9"

Python uses zero-based indexing:

x[0]    # 3
x[1]    # 50
x[2]    # 9
x[-1]   # 9

---

2. Vector Dimension

The dimension of a vector is the number of components it contains.

x = [4, 7, 2, 9]

Therefore:

[
\boxed{\dim(\mathbf{x}) = 4}
]

In Python:

len(x)

returns:

4

---

3. Changing a Component

Python lists are mutable, so we can change individual components.

x = [3, 50, 9]

x[1] = 100

The vector becomes:

[3, 100, 9]

---

4. Vector Addition

Vector addition is performed component by component.

Consider:

[
\mathbf{a} =
\begin{bmatrix}
3\
50\
9
\end{bmatrix}
\qquad
\mathbf{b} =
\begin{bmatrix}
1\
2\
4
\end{bmatrix}
]

Both vectors have dimension 3:

[
\dim(\mathbf{a}) = 3
]

[
\dim(\mathbf{b}) = 3
]

Therefore, addition is defined:

[
\mathbf{a}+\mathbf{b}

\begin{bmatrix}
3+1\
50+2\
9+4
\end{bmatrix}

\begin{bmatrix}
4\
52\
13
\end{bmatrix}
]

In Python:

a = [3, 50, 9]
b = [1, 2, 4]

The result is:

[4, 52, 13]

---

Important Rule

«Vector addition requires equal dimensions.»

For example:

a = [2, 4, 6]
b = [10, 20]

Here:

[
\dim(\mathbf{a}) = 3
]

[
\dim(\mathbf{b}) = 2
]

Since:

[
3 \ne 2
]

the vectors cannot be added.

---

5. Python Lists vs. Mathematical Vectors

A Python list's "+" operator does not perform mathematical vector addition.

[1, 2, 3] + [4, 5, 6]

produces:

[1, 2, 3, 4, 5, 6]

This is list concatenation.

Mathematical vector addition must be implemented component by component.

---

6. "vector_add()"

The implementation in "vector.py" is:

def vector_add(a, b):
    if len(a) == len(b):
        return [a[i] + b[i] for i in range(len(a))]
    else:
        raise ValueError("Vectors must have the same dimension.")

What it does

Step 1 — Check dimensions

len(a) == len(b)

Step 2 — Add corresponding components

[a[i] + b[i] for i in range(len(a))]

Step 3 — Reject incompatible vectors

raise ValueError("Vectors must have the same dimension.")

---

7. Why Vectors Matter in AI/Data Science

Vectors are one of the basic building blocks of AI and Data Science.

A data point can be represented as a vector of features:

[
\mathbf{x} =
\begin{bmatrix}
\text{age}\
\text{income}\
\text{experience}
\end{bmatrix}
]

For example:

x = [35, 60000, 8]

Here:

- "35" → age
- "60000" → income
- "8" → years of experience

The vector has dimension 3.

Vectors later become fundamental to:

- machine learning datasets
- feature representations
- linear regression
- neural networks
- embeddings
- optimization
- matrix operations

---

Key Takeaways

Vector

An ordered collection of numbers.

Dimension

The number of components in a vector.

Vector addition

Add corresponding components.

Compatibility

[
\boxed{\dim(\mathbf{a}) = \dim(\mathbf{b})}
]

is required for vector addition.

Python

A Python list is useful for representing a simple vector, but Python list operations do not automatically behave like mathematical vector operations.

---

Files

01_vectors/
├── README.md
└── vector.py

"vector.py" contains the Python implementation of the vector operations learned in this exercise.