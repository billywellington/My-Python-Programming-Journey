student_scores = [78, 65, 89, 86, 55, 91, 64, 89]

for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

highest_number = student_scores[0]  # Start with the first score as the highest

for score in student_scores:
    if score > highest_number:
        highest_number = score

print(f"The highest score in the class is: {highest_number}")
