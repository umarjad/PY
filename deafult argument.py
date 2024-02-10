import math

def calculate_cylinder_volume(radius=1, height=1):
    """
    Calculate the volume of a cylinder.

    Parameters:
    - radius (float): The radius of the cylinder. Default is 1.
    - height (float): The height of the cylinder. Default is 1.

    Returns:
    - float: The volume of the cylinder.
    """
    volume = math.pi * radius**2 * height
    return volume

# Example usage:
cylinder_volume_default = calculate_cylinder_volume()  # Using default values
print("Volume of cylinder with default values:", cylinder_volume_default)

cylinder_volume_custom = calculate_cylinder_volume(2, 5)  # Providing custom values
print("Volume of cylinder with custom values (radius=2, height=5):", cylinder_volume_custom)
