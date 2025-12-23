name = input("Enter you name: ")
score1 = float(input("Enter first test score: "))
score2 = float(input("Enter second test score: "))
score3 = float(input("Enter third test score: "))

End_Grade = (score3 + score2 + score1) / 3
if End_Grade > 89:
    grade = "an A"
elif End_Grade > 79:
    grade = "a B"
elif End_Grade > 59:
    grade = "a D"
else:
    grade = "an F"
print("\n--- Grade Report ---")
print(f"Student {name}")
print(f"Your Final Score is: {round(End_Grade, 1)} \nThat's {grade}")