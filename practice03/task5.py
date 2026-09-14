print("Mushka Vlad IT31")
day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))

if year <= 0:
    print("Date is invalid: year must be positive")

elif month < 1 or month > 12:
    print("Date is invalid: month must be between 1 and 12")

else:
    if month in [1, 3, 5, 7, 8, 10, 12]:
        max_day = 31
    elif month in [4, 6, 9, 11]:
        max_day = 30
    else:
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            max_day = 29
        else:
            max_day = 28

    if day < 1 or day > max_day:
        print(f"Date is invalid: month {month} has only {max_day} days")
    else:
        print("Date is valid")