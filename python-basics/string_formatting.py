"""
You will need to write a format string which prints out the data using the following syntax:
Hello John Doe. Your current balance is $53.44.
"""

data = ("John", "Doe", 53.44)
format_string = "Hello"

print(f"{format_string} {data[0]} {data[1]}, Your current balance is {data[2]}.")
