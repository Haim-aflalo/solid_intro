from open_closed.exercise_o1.classes.shape import Shape


class RectangleArea(Shape):
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width *self.height