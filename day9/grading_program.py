#!/usr/bin/env python3

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
"""
Scores 91 - 100: Grade = "Outstanding"

Scores 81 - 90: Grade = "Exceeds Expectations"

Scores 71 - 80: Grade = "Acceptable"

Scores 70 or lower: Grade = "Fail"
"""

for x in student_scores:
    score = student_scores[x]
    if score >= 91:
        student_grades[x] = "Outstanding"
    elif score >= 81 and score < 91:
        student_grades[x] = "Exceeds Expectations"
    elif score >= 71 and score < 81:
        student_grades[x] = "Acceptable"
    else:
        student_grades[x] = "Fail"


# 🚨 Don't change the code below 👇
print(student_grades)