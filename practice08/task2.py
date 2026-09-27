print("Mushka Vlad IT31")

schedule = {
    "Mon": [
        "Програмування",
        "Українська мова за професійним спрямуванням",
        "Адміністрування операційних систем та комп'ютерних мереж"
    ],

    "Tue": [
        "Програмування",
        "ІТ право",
        "Бази даних в інформаційних системах",
        "Фізкультура"
    ],

    "Wed": [
        "Іноземна мова за професійним спрямуванням",
        "Бази даних в інформаційних системах",
        "Бази даних в інформаційних системах / Розробка веб-ресурсів"
    ],

    "Thu": [
        "Програмування",
        "Розробка веб-ресурсів",
        "Адміністрування операційних систем та комп'ютерних мереж"
    ],

    "Fri": [
        "Іноземна мова за професійним спрямуванням",
        "Розробка веб-ресурсів",
        "ІТ право"
    ]
}


print("Розклад:")
for day, subjects in schedule.items():
    print(day, "|", len(subjects), "пар |", ", ".join(subjects))


total = sum(len(subjects) for subjects in schedule.values())
print("\nЗагальна кількість пар:", total)


busiest_day = max(schedule, key=lambda day: len(schedule[day]))
print("Найбільше пар:", busiest_day, "-", len(schedule[busiest_day]))


all_subjects = set()

for subjects in schedule.values():
    all_subjects.update(subjects)

print("\nУсі предмети:", all_subjects)
print("Кількість різних предметів:", len(all_subjects))


monday = set(schedule["Mon"])
wednesday = set(schedule["Wed"])

print("\nЄ і в понеділок, і в середу:", monday & wednesday)
print("Є в понеділок, але немає в середу:", monday - wednesday)


def count_subjects(schedule):
    result = {}

    for subjects in schedule.values():
        for subject in subjects:
            result[subject] = result.get(subject, 0) + 1

    return result


counts = count_subjects(schedule)

print("\nКількість пар кожного предмета:")
print(counts)


rating = sorted(counts.items(), key=lambda item: item[1], reverse=True)

print("\nРейтинг предметів:")

for number, (subject, count) in enumerate(rating, 1):
    print(f"{number}. {subject} — {count} пар")