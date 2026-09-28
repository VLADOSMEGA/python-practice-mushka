print("Mushka Vlad IT31")

about = (
    "My name is Mushka Vlad. "
    "I am a student of IT31. "
    "I study programming and computer technologies."
)

print("Початковий текст:")
print(about)

words = about.split()

print("\nКількість слів:", len(words))

longest_word = max(words, key=len)

print("Найдовше слово:", longest_word)

print("Слова у зворотному порядку:", " ".join(words[::-1]))

print("Кількість літер 'a':", about.lower().count("a"))

print("Текст з великих літер:", about.title())

print("Текст з підкресленнями:", about.replace(" ", "_"))


def is_palindrome(text):
    """
    Перевіряє, чи є текст паліндромом.
    Ігноруються пробіли та регістр.
    """
    cleaned = text.replace(" ", "").lower()

    return cleaned == cleaned[::-1]


print("\nПеревірка паліндрому:")
print(is_palindrome(about))


def caesar_cipher(text, shift):
    """
    Шифр Цезаря для латинських літер.
    """
    result = ""

    for char in text:
        if char.isalpha():
            if char.islower():
                result += chr((ord(char) - ord("a") + shift) % 26 + ord("a"))
            else:
                result += chr((ord(char) - ord("A") + shift) % 26 + ord("A"))
        else:
            result += char

    return result


shift = 3

encrypted = caesar_cipher(about, shift)

print("\nТекст після шифрування Цезарем:")
print(encrypted)