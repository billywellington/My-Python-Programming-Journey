# # numbers = [1, 2, 3]
# # new_list = [n + 1 for n in numbers]
# # # print(new_list)
# #
# # new_list = [n * 2 for n in range(1, 5)]
# # print(new_list)
# #
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
#
# new_names = [name.upper() for name in names if (len(name) > 5)]
# print(new_names)

students = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
import random

student_scores = {student:random.randint(50, 100) for student in students}
print(student_scores)

passed_students = {student:score for (student, score) in student_scores.items() if score > 70}
print(passed_students)