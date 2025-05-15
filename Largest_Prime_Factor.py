def largest(n):
    l = -1
 
    while n % 2 == 0:
        l = 2
        n //= 2

    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            l = i
            n //= i

    if n > 2:
        l = n

    return l

n =int(input("Enter the no.: "))
print("The largest prime factor is:", largest(n))
