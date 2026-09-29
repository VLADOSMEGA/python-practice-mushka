print("Mushka Vlad IT31")

me = {
    "name": "Vlad",
    "surname": "Mushka",
    "group": "IT31",
    "city": "Lutsk",
    "birth_year": "2009",
    "hobbies": ["cycling", "computer games", "swimming"]
}

print("Інформація про мене:")
for key, value in me.items():
    print(key, "-", value)

print("\nКлючі:", list(me.keys()))
print("Кількість пар:", len(me))

print("\nГрупа:", me["group"])
print("Email:", me.get("email", "unknown"))

# me["email"] викликало б помилку KeyError, оскільки такого ключа ще немає.

me["email"] = "vladmushka7@gmail.com"

me["city"] = "Lutsk"

removed_year = me.pop("birth_year")
print("\nВилучений рік народження:", removed_year)

print("\nСловник після змін:")
print(me)

print("\nЧи є ключ phone:", "phone" in me)