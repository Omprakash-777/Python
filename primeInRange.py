start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))
prime_list = []
for num in range(start, end + 1):
    if num > 1:  # 1 is not prime
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_list.append(num)
print("Range:", ",".join(str(p) for p in prime_list))