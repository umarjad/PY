def calculate_average(*args):
    """
    Calculate the average of an arbitrary number of numerical values.

    Parameters:
    - *args (float): Variable length of numerical values.

    Returns:
    - float: The average of the numerical values.
    """
    if len(args) == 0:
        return 0.0  # Return 0 if no arguments provided to avoid division by zero
    else:
        return sum(args) / len(args)

# Example usage:
average1 = calculate_average(5, 10, 15, 20)
print("Average 1:", average1)

average2 = calculate_average(2.5, 3.5, 4.5)
print("Average 2:", average2)

average3 = calculate_average()  # Calling the function without arguments
print("Average 3:", average3)
