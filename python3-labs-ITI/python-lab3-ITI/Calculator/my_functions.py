# Calculator/my_functions.py

def sum_numbers(a, b):
    return a + b

def subtract_numbers(a, b):
    if a == 0 or b == 0:
        raise ValueError("Subtracting zero from Number")
    return a - b

def divide_numbers(a, b):
    if b == 0:
        raise ZeroDivisionError("Can't divide with zero")
    return a / b

def multiply_numbers(a, b):
    if a == 0 or b == 0:
        raise ValueError("Multiply with Zero")
    return a * b
