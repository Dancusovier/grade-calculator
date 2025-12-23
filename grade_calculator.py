# ----------------------------------
# Project: Simple Grade Calculator
# Author: Your Name
# Description:
# This program asks the user for a test score
# and calculates the final grade.
# ----------------------------------

# Asks user for their name
name = input("Enter you name: ")

# Asks user for their Test grades
score1 = float(input("Enter first test score: "))
score2 = float(input("Enter second test score: "))
score3 = float(input("Enter third test score: "))

# Calculates final grade
End_Grade = (score3 + score2 + score1) / 3

# Assigns Letter Grade
if End_Grade > 89:
    grade = "an A"
elif End_Grade > 79:
    grade = "a B"
elif End_Grade > 59:
    grade = "a D"
else:
    grade = "an F"

# Displays the Grade Report
print("\n--- Grade Report ---")
print(f"Student {name}")
print(f"Your Final Score is: {round(End_Grade, 1)} \nThat's {grade}")