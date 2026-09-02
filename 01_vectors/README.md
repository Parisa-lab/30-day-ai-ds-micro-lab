01 — Vectors

AI/DS Micro-Lab · Mathematical Foundations

""Python" (https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)" (https://www.python.org/)
""Topic" (https://img.shields.io/badge/Topic-Linear%20Algebra-orange)"
""Level" (https://img.shields.io/badge/Level-Foundation-green)"

«Learning objective: Understand what vectors are, how their dimensions work, and how to implement vector addition in Python.»

---

Learning Path

Vector
  │
  ├── Components
  │
  ├── Dimension
  │
  ├── Indexing
  │
  ├── Modification
  │
  └── Addition
        │
        └── Dimension compatibility

---

1. What Is a Vector?

A vector is an ordered collection of numbers.

Mathematical view

[
\mathbf{x} =
\begin{bmatrix}
3\
50\
9
\end{bmatrix}
]

Python view

x = [3, 50, 9]

Think of the vector as a container whose position matters:

        Vector x

       ┌─────┐
x[0] → │  3  │
       ├─────┤
x[1] → │ 50  │
       ├─────┤
x[2] → │  9  │
       └─────┘

The order is important.

[3, 50, 9] ≠ [50, 3, 9]

---

2. Components

The individual numbers inside a vector are called components.

For:

x = [3, 50, 9]

we have:

Index| Component
"0"| "3"
"1"| "50"
"2"| "9"

Python uses zero-based indexing.

x[0]     # 3
x[1]     # 50
x[2]     # 9
x[-1]    # 9

«Key idea: "x[i]" means "the component at index "i"."»

---

3. Dimension

The dimension of a vector is the number of components it contains.

x = [4, 7, 2, 9]

There are four components:

[
\boxed{\dim(\mathbf{x}) = 4}
]

In Python:

len(x)

returns:

4

Visual intuition

[ 4 ] [ 7 ] [ 2 ] [ 9 ]
  ↑     ↑     ↑     ↑
  1     2     3     4

        dimension = 4

---

4. Changing a Component

Python lists are mutable.

That means we can change an existing component.

x = [3, 50, 9]

x[1] = 100

Before:

[ 3, 50, 9 ]
     ↑

After:

[ 3, 100, 9 ]
      ↑

The dimension has not changed.

[
\boxed{\dim(\mathbf{x}) = 3}
]

---

5. Vector Addition

Vector addition works component by component.

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

We add the corresponding components:

  3       1       4
 50   +   2   =  52
  9       4      13

Therefore:

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

Result:

[4, 52, 13]

---

6. Dimension Compatibility

There is one important condition:

[
\boxed{\dim(\mathbf{a}) = \dim(\mathbf{b})}
]

Vector addition is only defined when the dimensions are equal.

Valid

a = [3, 50, 9]
b = [1, 2, 4]

dimension(a) = 3
dimension(b) = 3

        ✓ Addition defined

Invalid

a = [2, 4, 6]
b = [10, 20]

dimension(a) = 3
dimension(b) = 2

        ✗ Addition not defined

Mathematically:

[
3 \ne 2
]

There is no corresponding component for the third element of "a".

---

7. Python Lists Are Not Mathematical Vectors

This is an important Python lesson.

You might expect:

[1, 2, 3] + [4, 5, 6]

to produce:

[5, 7, 9]

But Python produces:

[1, 2, 3, 4, 5, 6]

Why?

Because "+" for Python lists means concatenation.

List + List
    ↓
Concatenation

It does not automatically perform mathematical vector addition.

Therefore, we implement the mathematical operation ourselves.

---

8. Implementing Vector Addition

def vector_add(a, b):
    if len(a) == len(b):
        return [a[i] + b[i] for i in range(len(a))]
    else:
        raise ValueError("Vectors must have the same dimension.")

How it works

① Check dimensions

len(a) == len(b)

② Add corresponding components

[a[i] + b[i] for i in range(len(a))]

③ Reject incompatible vectors

raise ValueError("Vectors must have the same dimension.")

---

9. Why "ValueError"?

Suppose:

a = [1, 2, 3]
b = [4, 5]

The vectors have different dimensions:

[
3 \ne 2
]

So the operation is invalid.

Instead of silently producing a wrong result, the program explicitly stops and reports the problem:

ValueError: Vectors must have the same dimension.

This is preferable to simply printing ""Error"" because Python knows that the function encountered invalid input.

---

10. Vectors in AI & Data Science

Vectors are fundamental to AI and Data Science.

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

This represents:

┌───────────────┐
│ Age        35 │
│ Income  60000 │
│ Experience  8 │
└───────────────┘

So:

[
\boxed{\dim(\mathbf{x}) = 3}
]

Vectors will later appear everywhere:

Vectors
   │
   ├── Features
   ├── Data points
   ├── Model parameters
   ├── Embeddings
   ├── Neural-network activations
   └── Optimization

---

11. Mini Practice

Exercise 1

What is the dimension?

x = [8, 3, 11, 6, 2]

Answer:

[
\boxed{5}
]

---

Exercise 2

What is "x[-1]"?

x = [8, 3, 11, 6, 2]

Answer:

2

---

Exercise 3

Can these vectors be added?

a = [1, 2, 3]
b = [4, 5]

Answer:

No.

because:

[
\dim(\mathbf{a}) = 3
]

[
\dim(\mathbf{b}) = 2
]

and:

[
3 \ne 2
]

---

Key Rules

Concept| Rule
Vector| Ordered collection of numbers
Component| Individual number in a vector
Dimension| Number of components
Python indexing| Starts at "0"
"x[-1]"| Last component
List mutation| Components can be changed
Vector addition| Add corresponding components
Addition requirement| Dimensions must be equal
Python list "+"| Concatenates lists
Invalid dimensions| Raise "ValueError"

---

Project Structure

30-day-ai-ds-micro-lab/
│
├── 01_vectors/
│   ├── README.md
│   └── vector.py
│
└── ...

---

Foundation Principle

«Before performing an operation on vectors, always check that their dimensions are compatible.»

This habit will become increasingly important when we move from vectors to matrices, neural networks, and machine-learning models.