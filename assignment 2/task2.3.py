import math

def calculate_area(shape, **kwargs):
    """
    Calculate the area of different shapes.
    Supported shapes: circle, rectangle, triangle, square
    """
    shape = shape.lower()

    if shape == "circle":
        radius = kwargs.get("radius")
        if radius is None:
            return "❌ Please provide 'radius' for circle"
        return math.pi * radius ** 2

    elif shape == "rectangle":
        length = kwargs.get("length")
        width = kwargs.get("width")
        if None in (length, width):
            return "❌ Please provide 'length' and 'width' for rectangle"
        return length * width

    elif shape == "triangle":
        base = kwargs.get("base")
        height = kwargs.get("height")
        if None in (base, height):
            return "❌ Please provide 'base' and 'height' for triangle"
        return 0.5 * base * height

    elif shape == "square":
        side = kwargs.get("side")
        if side is None:
            return "❌ Please provide 'side' for square"
        return side ** 2

    else:
        return "❌ Unsupported shape! Try: circle, rectangle, triangle, or square"


# ✅ Example usage:
print("Area of circle:", calculate_area("circle", radius=5))
print("Area of rectangle:", calculate_area("rectangle", length=10, width=6))
print("Area of triangle:", calculate_area("triangle", base=8, height=4))
print("Area of square:", calculate_area("square", side=7))
