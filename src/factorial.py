"""
This program computes the factorial of a number.
"""
def factorial(number):
    """
    This function implements factorial.
    """
    result = 1

    while number > 1:
        result *= number
        number -= 1

    return result

print(factorial(4))
