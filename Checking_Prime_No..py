n = int(input("Enter a number: "))
    
if n <= 1:
    print(f"{n} is not a prime number.")
    
else:
    number = True
   
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            number = False
            break

    if number:
        print("True")
    else:
        print("Fa)lse")
