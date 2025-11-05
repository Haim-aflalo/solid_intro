import math
from open_closed.exercise_o1.classes.shape import Shape


class CircleArea(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius**2
