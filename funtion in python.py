def calculate_rectangle_area(length, width):
    """
    Calculate the area of a rectangle.

    Parameters:
    - length (float): The length of the rectangle.
    - width (float): The width of the rectangle.

    Returns:
    - float: The area of the rectangle.
    """
    area = length * width
    return area

# Example usage:
length = 5.0
width = 3.0
area = calculate_rectangle_area(length, width)
print("Area of rectangle:", area)
