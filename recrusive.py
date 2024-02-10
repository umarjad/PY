def factorial(n):
    """
    Calculate the factorial of a non-negative integer using recursion.

    Parameters:
    - n (int): The non-negative integer.

    Returns:
    - int: The factorial of the input integer.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Example usage:
number = 5
result = factorial(number)
print("Factorial of", number, "is", result)
