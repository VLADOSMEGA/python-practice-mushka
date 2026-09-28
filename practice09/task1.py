print("Mushka Vlad IT31")

full_name = "   МУШКА    владислав  мИХАЙЛОВИЧ  "

full_name = full_name.strip()

parts = full_name.split()

parts = [part.capitalize() for part in parts]

full_name = " ".join(parts)

print("Виправлений ПІБ:", full_name)

surname, name, patronymic = parts

print("Прізвище:", surname)
print("Ім'я:", name)
print("По Батькові:", patronymic)

print("ПІБ у верхньому регістрі:", full_name.upper())
print("ПІБ у нижньому регістрі:", full_name.lower())
print("Кількість символів:", len(full_name))

print("Перший символ:", full_name[0])
print("Останній символ:", full_name[-1])

print("ПІБ навпаки:", full_name[::-1])

print("З підкресленнями:", full_name.replace(" ", "_"))