print("Vlad Mushka, IT31")
def get_initials(name: str, surname: str) -> str:
    return f"{name[0].upper()}.{surname[0].upper()}."


def count_letters(text: str, letter: str = "a") -> int:
    """Return how many times letter occurs in text."""
    count = 0

    for char in text.lower():
        if char == letter.lower():
            count += 1

    return count


def count_vowels(text: str) -> int:
    vowels = 0

    for char in text.lower():
        if char in "aeiouy":
            vowels += 1

    return vowels


def reverse_text(text: str) -> str:
    reversed_text = ""

    for char in text:
        reversed_text = char + reversed_text

    return reversed_text


name = "Vlad"
surname = "Mushka"
c = 6

print("Vlad Mushka, IT31")

print(f"Full name: {name} {surname}")
print(f"Initials: {get_initials(name, surname)}")

vowels = count_vowels(surname)
consonants = c - vowels

print(f"Letters in surname: {c}")
print(f"Vowels: {vowels}, consonants: {consonants}")

for vowel in "aeiou":
    amount = count_letters(surname, letter=vowel)
    print(f"{vowel}: {amount}")

print(f"Default letter 'a': {count_letters(surname)}")

print(f"Reversed surname: {reverse_text(surname)}")

print(f"Docstring: {count_letters.__doc__}")
print(f"Annotations: {count_letters.__annotations__}")