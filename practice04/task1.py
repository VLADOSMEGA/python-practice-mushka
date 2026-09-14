print("Mushka Vlad IT31")

d = 17
c = 6

print("числовий ряд від дня народження методом 'for':")
print(f"Numbers from {d} to 31:", end=" ")

count = 0
total = 0
product = 1
even = 0
odd = 0

for i in range(d, 32):
    print(i, end=" ")
    count += 1
    total += i
    product *= i

    if i % 2 == 0:
        even += 1
    else:
        odd += 1

print()
print(f"Count: {count}")
print(f"Sum: {total}")
print(f"Product: {product}")
print(f"Average: {total / count:.2f}")
print(f"Even: {even}, odd: {odd}")

print("числовий ряд від дня народження методом 'while':")

count = 0
total = 0
product = 1
even = 0
odd = 0
i = d

while i <= 31:
    count += 1
    total += i
    product *= i

    if i % 2 == 0:
        even += 1
    else:
        odd += 1

    i += 1

print("While version:")
print(f"Count: {count}")
print(f"Sum: {total}")
print(f"Product: {product}")
print(f"Average: {total / count:.2f}")
print(f"Even: {even}, odd: {odd}")

print("Countdown:", end=" ")

for i in range(c, 0, -1):
    print(i, end=" ")

print()