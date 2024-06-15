student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆
# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}


# TODO-2: Write your code below to add the grades to student_grades.👇
for key in student_scores:
    value = student_scores[key]
    if 91 <= value <= 100:
        student_grades[key] = "Outstanding"
    elif 81 <= value <= 90:
        student_grades[key] = "Exceeds Expectations"
    elif 71 <= value <= 80:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"


# 🚨 Don't change the code below 👇
print(student_grades)