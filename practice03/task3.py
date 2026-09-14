print("Mushka Vlad IT31")
first_number = float(input("Enter the first number: "))
operation = input("Enter operation (+, -, *, /, //, %, **): ")
second_number = float(input("Enter the second number: "))

if operation == "+":
    result = first_number + second_number
    print(f"{first_number} + {second_number} = {result:.4f}")

elif operation == "-":
    result = first_number - second_number
    print(f"{first_number} - {second_number} = {result:.4f}")

elif operation == "*":
    result = first_number * second_number
    print(f"{first_number} * {second_number} = {result:.4f}")

elif operation == "/":
    if second_number == 0:
        print("Error: division by zero")
    else:
        result = first_number / second_number
        print(f"{first_number} / {second_number} = {result:.4f}")

elif operation == "//":
    if second_number == 0:
        print("Error: division by zero")
    else:
        result = first_number // second_number
        print(f"{first_number} // {second_number} = {result:.4f}")

elif operation == "%":
    if second_number == 0:
        print("Error: division by zero")
    else:
        result = first_number % second_number
        print(f"{first_number} % {second_number} = {result:.4f}")

elif operation == "**":
    result = first_number ** second_number
    print(f"{first_number} ** {second_number} = {result:.4f}")

else:
    print("Unknown operation")