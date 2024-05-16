# Python Programming

:snake: Python - Classes and Objects
---
## Tasks

### [0. My first square](https://github.com/WennieL/holbertonschool-higher_level_programming/blob/master/python-classes/0-square.py)
Write an empty class `Square` that defines a square:

### [1. Square with size](https://github.com/WennieL/holbertonschool-higher_level_programming/blob/master/python-classes/1-square.py)
Write a class `Square` that defines a square by: (based on [0-square.py](https://github.com/WennieL/holbertonschool-higher_level_programming/blob/master/python-classes/0-square.py))

- Private instance attribute: `size`
- Instantiation with `size` (no type/value verification)
- You are not allowed to import any module

### [2. Size validation](https://github.com/WennieL/holbertonschool-higher_level_programming/blob/master/python-classes/2-square.py)
Write a class `Square` that defines a square by: (based on [1-square.py](https://github.com/WennieL/holbertonschool-higher_level_programming/blob/master/python-classes/1-square.py))

- Private instance attribute: `size`
- Instantiation with optional `size: def __init__(self, size=0):`
    - `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
    - if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`

### [3. Area of a square](https://github.com/WennieL/holbertonschool-higher_level_programming/blob/master/python-classes/3-square.py)
Write a class `Square` that defines a square by: (based on [2-square.py](https://github.com/WennieL/holbertonschool-higher_level_programming/blob/master/python-classes/2-square.py))

- Private instance attribute: `size`
- Instantiation with optional `size: def __init__(self, size=0):`
    - `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
    - if `siz`e is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`
- Public instance method: `def area(self):` that returns the current square area

### [4. Access and update private attribute](https://github.com/WennieL/holbertonschool-higher_level_programming/blob/master/python-classes/4-square.py)
Write a class `Square`that defines a square by: (based on [3-square.py](https://github.com/WennieL/holbertonschool-higher_level_programming/blob/master/python-classes/3-square.py))

- Private instance attribute: `size:`
    - property `def size(self):` to retrieve it
    - property setter `def size(self, value):` to set it:
        - `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
        - if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`
- Instantiation with optional `size: def __init__(self, size=0):`
- Public instance method: `def area(self):` that returns the current square area


### [5. Printing a square](https://github.com/WennieL/holbertonschool-higher_level_programming/blob/master/python-exceptions/5-raise_exception.py)
Write a class `Square` that defines a square by: (based on [4-square.py](https://github.com/WennieL/holbertonschool-higher_level_programming/blob/master/python-classes/4-square.py))

- Private instance attribute: `size:`
    - property def size(self): to retrieve it
    - property setter `def size(self, value):` to set it:
        - `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
        - if `size` is less than `0`, raise a `ValueError` exception with the message `size must `be >= 0`
- Instantiation with optional `size: def __init__(self, size=0):`
- Public instance method: `def area(self):` that returns the current square area
- Public instance method: `def my_print(self):` that prints in stdout the square with the character `#`:
    - if `size` is equal to 0, print an empty line

### [6. Coordinates of a square](https://github.com/WennieL/holbertonschool-higher_level_programming/blob/master/python-classes/6-square.py)
Write a class `Square` that defines a square by: (based on [5-square.p](https://github.com/WennieL/holbertonschool-higher_level_programming/blob/master/python-exceptions/5-raise_exception.py))

- Private instance attribute: `size:`
    - property `def size(self):` to retrieve it
    - property setter `def size(self, value):` to set it:
        - `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
        - if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`
- Private instance attribute: `position:`
    - property `def position(self):` to retrieve it
    - property setter `def position(self, value):` to set it:
        - `position` must be a tuple of 2 positive integers, otherwise raise a `TypeError` exception with the message `position must be a tuple of 2 positive integers`
- Instantiation with optional `size` and optional `position: def __init__(self, size=0, position=(0, 0)):`
- Public instance method: `def area(self):` that returns the current square area
- Public instance method: `def my_print(self):` that prints in stdout the square with the character `#:`
        - if `size` is equal to 0, print an empty line
        - `position` should be use by using space - <b>Don’t fill lines</b> by spaces when `position[1] > 0`