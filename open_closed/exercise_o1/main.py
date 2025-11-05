from classes.square import SquareArea
from open_closed.exercise_o1.classes.circle import CircleArea
from open_closed.exercise_o1.classes.rectangle import RectangleArea

if __name__ == "__main__":
    s = SquareArea(9)
    print(s.calculate_area())
    r = RectangleArea(2,4)
    print(r.calculate_area())
    c = CircleArea(4)
    print(c.calculate_area())
