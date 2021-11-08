"""
In this exercise, you will need to print an alphabetically sorted list of all functions in the re module,
which contain the word find.
"""

import re


for function_with_find in dir(re):
    if "find" in function_with_find:
        print(function_with_find)
