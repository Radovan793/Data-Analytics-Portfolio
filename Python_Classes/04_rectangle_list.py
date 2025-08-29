# Rectangle class with area calculation for multiple objects.

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height


# List of rectangle objects
rectangles = [
    Rectangle(52, 23),
    Rectangle(18, 32),
    Rectangle(63, 25),
    Rectangle(53, 41),
    Rectangle(32, 51)
]

# Print areas
for i, rect in enumerate(rectangles, 1):
    print(f"Rectangle {i}: Area = {rect.get_area()}")
