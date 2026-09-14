print("Mushka Vlad IT31")
score = int(input("Enter your score (0-100): "))
missed = int(input("Enter missed lessons: "))

if score < 0 or score > 100:
    print("Error: score must be between 0 and 100")
else:
    if score >= 90:
        grade = "A"
    elif score >= 82:
        grade = "B"
    elif score >= 74:
        grade = "C"
    elif score >= 64:
        grade = "D"
    elif score >= 60:
        grade = "E"
    else:
        grade = "F"

    if missed > 16 * 0.30:
        passed = "failed"
        print("Warning: too many missed lessons")
    elif score >= 60:
        passed = "passed"
    else:
        passed = "failed"

    print(f"Score: {score}, Grade: {grade}, Result: {passed}")