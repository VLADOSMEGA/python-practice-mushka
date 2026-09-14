print("Vlad Mushka, IT31")
def print_card():
    print("Name: Vlad Mushka")
    print("Group: IT31")
    print("Birth year: 2009")

print("no parameters, call 1")
print_card()

print("no parameters, call 2")
print_card()

print("no parameters, call 3")
print_card()


def print_card_args(name, surname, year, group="IT31"):
    print(f"{name} {surname}, {group}, {year}")


print("positional arguments")
print_card_args("Vlad", "Mushka", 2009, "IT31")

print("keyword arguments")
print_card_args(
    surname="Mushka",
    name="Vlad",
    group="IT31",
    year=2009
)

print("mixed arguments")
print_card_args("Vlad", "Mushka", year=2009, group="IT31")

print("default group")
print_card_args("Vlad", "Mushka", 2009)