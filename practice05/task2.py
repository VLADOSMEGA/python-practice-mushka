print("Vlad Mushka, IT31")
def print_age(year):
    age = 2026 - year
    print(f"Age: {age}")


def get_age(year, current_year=2026):
    if year > current_year or year < 0:
        return -1

    return current_year - year

    print("after return")

y = 2009

print_age(y)

print(f"print_age returned: {print_age(y)}")

age = get_age(y)

print(f"Age from get_age: {age}")
print(f"Age in months: {age * 12}")
print(f"Age in weeks: {age * 52}")

age_2030 = get_age(y, 2030)
print(f"Age in 2030: {age_2030}")

invalid_age = get_age(3000)
print(f"Invalid year 3000 gives: {invalid_age}")