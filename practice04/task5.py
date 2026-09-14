print("Vlad Mushka, IT31")
d = 17
c = 6

n = d * c

print(f"n = {d} * {c} = {n}")

print("Divisors:", end=" ")

count = 0
total = 0

for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=" ")
        count += 1
        total += i

print()
print(f"Divisors count: {count}")
print(f"Divisors sum: {total}")

for i in range(2, n):
    if n % i == 0:
        print(f"{n} is not prime")
        break
else:
    print(f"{n} is prime")

print(f"Primes up to {n}:", end=" ")

primes_count = 0

for number in range(2, n + 1):
    for i in range(2, number):
        if number % i == 0:
            break
    else:
        print(number, end=" ")
        primes_count += 1

print()
print(f"Primes count: {primes_count}")