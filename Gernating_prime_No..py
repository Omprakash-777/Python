n = int(input("Enter the number of primes to generate: "))
p = []
num = 2

while len(p) < n:
    prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            prime = False
            break
    if prime:
        p.append(num)
    num += 1

print("First", n, "prime numbers:", p)
