from single_responsibility.exercise_2.classes.average_grade import CalculateGrade
from single_responsibility.exercise_2.classes.student import Student

s = Student("haim",[20,10])
print(CalculateGrade.calculate_average_grade(s.grades))