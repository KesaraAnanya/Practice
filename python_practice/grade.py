def grade(score):
    if score <0 and score > 100:
        if score >= 90:
            grade = "A"
        elif score >= 80:
            grade = "B"
        elif score >= 70:
            grade = "C"
        else:
            grade = "F"
        return grade
    else:
        return "INVALID"

score = int(input("Enter score:"))
print("Grade:",grade(score))
