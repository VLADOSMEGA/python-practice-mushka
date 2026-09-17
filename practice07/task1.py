print("Mushka Vlad IT31")

grades = [10, 8, 8, 9, 10, 8]

print("Оцінки:", grades)
print("Кількість оцінок:", len(grades))
print("Сума оцінок:", sum(grades))
print("Найкраща оцінка:", max(grades))
print("Найгірша оцінка:", min(grades))

average = sum(grades) / len(grades)
print("Середній бал:", round(average, 2))

sorted_grades = sorted(grades, reverse=True)
print("Оцінки від найкращої до найгіршої:", sorted_grades)
print("Початковий список:", grades)

print("3 найкращі оцінки:", sorted_grades[:3])
print("3 найгірші оцінки:", sorted_grades[-3:])

worst_position = grades.index(min(grades)) + 1
print("Позиція найгіршої оцінки:", worst_position)

above_average = [grade for grade in grades if grade > average]
print("Оцінки вище середнього:", above_average)
print("Кількість оцінок вище середнього:", len(above_average))

print("Чи є оцінка 12:", 12 in grades)
print("Чи є оцінка 1:", 1 in grades)

new_grade = 6 % 12 + 1
grades.append(new_grade)
print("Після append:", grades)

grades.insert(0, 12)
print("Після insert:", grades)

grades.remove(min(grades))
print("Після видалення найгіршої оцінки:", grades)

removed_grade = grades.pop()
print("Видалена остання оцінка:", removed_grade)
print("Після pop:", grades)

print("Кількість оцінок 12:", grades.count(12))

result = grades.sort()
print("Результат sort():", result)
print("Список після sort():", grades)