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

# Assigning a different name to the function
factorial_alternative = factorial

# Example usage using the original and alternative names
number = 5
result_original = factorial(number)
result_alternative = factorial_alternati
