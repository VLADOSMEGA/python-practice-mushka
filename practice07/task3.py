print("Mushka Vlad IT31")

def print_subjects(subjects):
    print("Предмети:")

    for number, subject in enumerate(subjects, 1):
        title, pairs, grade = subject
        print(f"{number}. {title} — {pairs} пари, оцінка {grade}")


def total_pairs(subjects):
    total = 0

    for subject in subjects:
        total += subject[1]

    return total


def subject_with_most_pairs(subjects):
    return max(subjects, key=lambda subject: subject[1])


def subject_with_lowest_grade(subjects):
    return min(subjects, key=lambda subject: subject[2])


def get_titles(subjects):
    return [subject[0] for subject in subjects]


def get_grades(subjects):
    return [subject[2] for subject in subjects]


def average_grade(grades):
    return sum(grades) / len(grades)


def print_high_grades(subjects):
    print("Предмети з оцінкою 10+:")
    
    for subject in subjects:
        if subject[2] >= 10:
            print(subject[0])


def print_histogram(subjects):
    print("Гістограма оцінок:")

    for subject in subjects:
        print(f"{subject[0]}: {'#' * subject[2]}")


def retake_lowest_grade(subjects):
    lowest = subject_with_lowest_grade(subjects)

    updated_subjects = []

    for subject in subjects:
        if subject == lowest:
            new_grade = min(subject[2] + 2, 12)
            updated_subjects.append((subject[0], subject[1], new_grade))
        else:
            updated_subjects.append(subject)

    return updated_subjects


def main():
    subjects = [
        ("Ukrainian Language for Professional Purposes", 1, 8),
        ("Operating Systems and Computer Networks Administration", 2, 10),
        ("Foreign Language for Professional Purposes", 2, 10),
        ("IT Law", 2, 8)
    ]

    print_subjects(subjects)

    print()
    print("Загальна кількість пар на тиждень:", total_pairs(subjects))

    most_pairs = subject_with_most_pairs(subjects)
    print("Найбільше пар:", most_pairs[0], "-", most_pairs[1])

    lowest_grade = subject_with_lowest_grade(subjects)
    print("Найнижча оцінка:", lowest_grade[0], "-", lowest_grade[2])

    titles = get_titles(subjects)
    grades = get_grades(subjects)

    print()
    print("Список назв предметів:", titles)
    print("Список оцінок:", grades)
    print("Середній бал:", round(average_grade(grades), 2))

    print()
    print_high_grades(subjects)

    print()
    print_histogram(subjects)

    print()
    print("Після перездачі найнижчої оцінки:")

    subjects = retake_lowest_grade(subjects)
    print_subjects(subjects)


main()