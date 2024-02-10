def calculate_addition(a, b):
    """
    Calculate the addition of two numbers using an inner function.

    Parameters:
    - a (int or float): The first number.
    - b (int or float): The second number.

    Returns:
    - int or float: The result of the addition.
    """
    def add(x, y):
        return x + y
    
    result = add(a, b)
    return result

# Example usage:
num1 = 10
num2 = 5
addition_result = calculate_addition(num1, num2)
print("Result of addition:", addition_result)
