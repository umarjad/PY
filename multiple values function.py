def calculate_rectangle_properties(length, width):
    """
    Calculate properties of a rectangle.

    Parameters:
    - length (float): The length of the rectangle.
    - width (float): The width of the rectangle.

    Returns:
    - tuple: A tuple containing the area and perimeter of the rectangle.
    """
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

# Example usage:
rectangle_length = 5.0
rectangle_width = 3.0
rectangle_area, rectangle_perimeter = calculate_rectangle_properties(rectangle_length, rectangle_width)

print("Area of rectangle:", rectangle_area)
print("Perimeter of rectangle:", rectangle_perimeter)
