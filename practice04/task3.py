print("Mushka Vlad IT31")

name = "Vlad"
surname = "Mushka"

text = name + surname

vowels = 0
consonants = 0

for letter in text:
    if letter.lower() in "aeiouy":
        vowels += 1
    else:
        consonants += 1

print(f"{name} {surname}")
print(f"Vowels: {vowels}, Consonants: {consonants}")
print(f"Total letters: {len(text)}")