Vector Basics

This folder contains the first AI/Data Science foundation exercise of the 30-Day AI/DS Micro-Lab.

What is a Vector?

A vector is an ordered collection of numbers.

For example:

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

The vector above has 3 components, so its dimension is 3.

Vector Components

Python uses zero-based indexing:

x[0]  # 3
x[1]  # 50
x[2]  # 9

The last component can also be accessed with negative indexing:

x[-1]  # 9

Changing a Component

Python lists are mutable, so a component can be changed:

x[1] = 100

The vector becomes:

[3, 100, 9]

Vector Addition

Two vectors can be added only when they have the same dimension.

For example:

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

Both vectors have dimension 3, so addition is defined:

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

Important Rule

[
\boxed{\text{Vector addition requires equal dimensions.}}
]

For example:

a = [2, 4, 6]  # dimension 3
b = [10, 20]   # dimension 2

These vectors cannot be added because:

[
3 \ne 2
]

Python Implementation

Mathematical vector addition must be implemented component by component. Python's "+" operator for lists performs concatenation, not mathematical vector addition.

def vector_add(a, b):
    if len(a) == len(b):
        return [a[i] + b[i] for i in range(len(a))]
    else:
        raise ValueError("Vectors must have the same dimension.")

The function:

1. Checks whether the two vectors have the same dimension.
2. Adds corresponding components when the dimensions match.
3. Raises a "ValueError" when the dimensions are different.

Current Learning Goal

The goal of this exercise is to understand the connection between:

mathematical vectors → vector dimensions → Python lists → component-wise operations.