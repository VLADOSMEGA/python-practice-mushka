print("Mushka Vlad IT31")

surname = "Mushka"
c = 6

letters = list(surname.lower())

print("Список літер:", letters)
print("Довжина списку:", len(letters))

print("Перша літера:", letters[0])
print("Середня літера:", letters[len(letters) // 2])
print("Остання літера:", letters[-1])
print("Остання літера другим способом:", letters[len(letters) - 1])

print("Перші 3 літери:", letters[:3])
print("Усі літери, крім перших 3:", letters[3:])
print("Кожна друга літера:", letters[::2])
print("У зворотному порядку:", letters[::-1])
print("Останні 2 літери:", letters[-2:])

print("5 літер, починаючи з позиції c:", letters[c:c + 5])

unique = []

for letter in letters:
    if letter not in unique:
        unique.append(letter)

print("Унікальні літери:", unique)

repeated = False

for letter in unique:
    count = letters.count(letter)

    if count > 1:
        print(f"Літера '{letter}' повторюється {count} рази")
        repeated = True

if not repeated:
    print("No repeated letters")

print("Літери в алфавітному порядку:", sorted(letters))