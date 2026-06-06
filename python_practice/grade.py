def grade(score):
    while score in range(0,101):
        if score >= 90:
            grade = "A"
        elif score >= 80:
            grade = "B"
        elif score >= 70:
            grade = "C"
        else:
            grade = "F"
        return grade

score = int(input("Enter score:"))
print("Grade:",grade(score))
