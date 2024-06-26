# :snake: Python - Test-driven development

![image](https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/246/giphy-4.gif)

## Tasks

### [0. Integers addition](https://github.com/WennieL/holbertonschool-higher_level_programming/blob/master/python-test_driven_development/0-add_integer.py)
### [tests/0-add_integer.txt](https://github.com/WennieL/holbertonschool-higher_level_programming/blob/master/python-test_driven_development/tests/0-add_integer.txt)

Write a function that adds 2 integers.

- Prototype: `def add_integer(a, b=98):`
- `a` and `b` must be integers or floats, otherwise raise a `TypeError` exception with the message `a must be an integer` or `b must be an integer`
- `a` and `b` must be first casted to integers if they are float
- Returns an integer: the addition of `a` and `b`

### [1. Divide a matrix](https://github.com/WennieL/holbertonschool-higher_level_programming/blob/master/python-test_driven_development/2-matrix_divided.py)
### [tests/2-matrix_divided.txt](https://github.com/WennieL/holbertonschool-higher_level_programming/blob/master/python-test_driven_development/tests/2-matrix_divided.txt)

Write a function that divides all elements of a matrix.

- Prototype: `def matrix_divided(matrix, div):`
- `matrix` must be a list of lists of integers or floats, otherwise raise a `TypeError` exception with the message `matrix must be a matrix (list of lists) of integers/floats`
- Each row of the `matrix` must be of the same size, otherwise raise a `TypeError` exception with the message `Each row of the matrix must have the same size`
- `div` must be a number (integer or float), otherwise raise a `TypeError` exception with the message `div must be a number`
- `div` can’t be equal to `0`, otherwise raise a `ZeroDivisionError` exception with the message `division by zero`
- All elements of the matrix should be divided by `div`, rounded to 2 decimal places
- Returns a new matrix

### [2. Say my name](https://github.com/WennieL/holbertonschool-higher_level_programming/blob/master/python-test_driven_development/3-say_my_name.py)
### [tests/3-say_my_name.txt](https://github.com/WennieL/holbertonschool-higher_level_programming/blob/master/python-test_driven_development/tests/3-say_my_name.txt)

Write a function that prints `My name is <first name> <last name>`

- Prototype: `def say_my_name(first_name, last_name=""):`
- `first_name` and `last_name` must be strings otherwise, raise a `TypeError` exception with the message `first_name must be a strin`g` or `last_name must be a string`

### [3. Print square](https://github.com/WennieL/holbertonschool-higher_level_programming/blob/master/python-test_driven_development/4-print_square.py)
### [tests/3-say_my_name.txt](https://github.com/WennieL/holbertonschool-higher_level_programming/blob/master/python-test_driven_development/tests/4-print_square.txt)

Write a function that prints a square with the character `#`.

- Prototype: `def print_square(size):`
- `size` is the size length of the square
- `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
- if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`
- if `size` is a float and is less than 0, raise a `TypeError` exception with the message `size must be an integer`

### [4. Text indentation]()
### [tests/5-text_indentation.txt]()

Write a function that prints a text with 2 new lines after each of these characters: `.`, `?` and `:`

Prototype: `def text_indentation(text):`
`text` must be a string, otherwise raise a `TypeError` exception with the message `text must be a string`
There should be no space at the beginning or at the end of each printed line

### [5. Max integer - Unittest](https://github.com/WennieL/holbertonschool-higher_level_programming/blob/master/python-test_driven_development/tests/6-max_integer_test.py)

Since the beginning you have been creating “Interactive tests”. 
For this exercise, you will add Unittests.

In this task, you will write unittests for the function `def max_integer(list=[]):.`

- Your test file should be inside a folder `tests`
- You have to use the [unittest module](https://docs.python.org/3.4/library/unittest.html#module-unittest)
- Your test file should be python files (extension: `.py`)
- Your test file should be executed by using this command: `python3 -m unittest tests.6-max_integer_test`
- All tests you make must be passable by the function below
- We strongly encourage you to work together on test cases, so that you don’t miss any edge case