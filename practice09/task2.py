print("Mushka Vlad IT31")

grades_text = "10, 8, 8, 9, 10, 8"

grades = [int(grade) for grade in grades_text.split(", ")]

print("Початковий рядок:", grades_text)
print("Список оцінок:", grades)

print("Кількість оцінок:", len(grades))
print("Сума оцінок:", sum(grades))
print("Найвища оцінка:", max(grades))
print("Найнижча оцінка:", min(grades))

average = sum(grades) / len(grades)

print(f"Середній бал: {average:.2f}")

above_average = [grade for grade in grades if grade > average]

print("Оцінки вище середнього:", above_average)

grades_string = " | ".join(str(grade) for grade in grades)

print("Оцінки через |:", grades_string)

print("Оцінки за зростанням:", sorted(grades))
print("Оцінки за спаданням:", sorted(grades, reverse=True))

print("Кількість оцінок 10:", grades.count(10))