from open_closed.exercise_o1.classes.shape import Shape

class SquareArea(Shape):
    def __init__(self,side):
        self.side = side

    def calculate_area(self):
        return self.side ** 2
