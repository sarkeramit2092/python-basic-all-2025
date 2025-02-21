1. Module 🟦
A module is simply a single Python file (.py) that contains variables, functions, and classes.

# module1.py
def greet():
    return "Hello, World!"

To use it:
import module1
print(module1.greet())  # Output: Hello, World!

2. Package 📦
A package is a directory that contains multiple modules.
It must include a special __init__.py file to be recognized as a package.

Example structure:

mypackage/
├── __init__.py
├── module1.py
├── module2.py
Using a package:
from mypackage import module1
print(module1.greet())

3. Library 📚
A library is a collection of packages and modules.
Example: matplotlib, numpy, pandas
Libraries can be installed using pip:

pip install numpy
Using a library:

import numpy as np
arr = np.array([1, 2, 3])
print(arr)


4. Script vs. Module vs. Library
Term	Definition
Script	A Python file intended to be executed (e.g., main.py).
Module	A Python file (.py) containing reusable code (functions, classes, etc.).
Package	A directory containing multiple modules and an __init__.py file.
Library	A collection of packages and modules (e.g., requests, matplotlib).


Real-World Example: matplotlib
matplotlib is a library.
Inside matplotlib, there are packages like matplotlib.backends.
Inside the package, there are modules like backend_qt5.py.