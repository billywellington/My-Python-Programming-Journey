# Exercise 5: Modeling a Student Class
# Question:
# Define a Python class named Student to represent a student in a school. The Student class should have:
#
# Attributes for name, age, and grade.
# A method named promote() that increments the student's grade by 1.

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def promote(self):
        self.new_grade = self.grade + 1
        print(f"{self.name} aged {self.age} has been promoted from grade {self.grade} to grade {self.new_grade}")

student1 = Student("Martha", 12, 6)
student2 = Student("Alice", 13, 7)
student3 = Student("Boyle", 14, 8)
student4 = Student("Steve", 15, 9)

student1.promote()
student2.promote()
student3.promote()
student4.promote()