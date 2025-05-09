num=int(input("Enter a number: "))
if num<=1:
    print(num,"is not a prime number")
else:
    temp=True
    for i in range(2,round(num**0.5)+1):
        if num % i == 0:
            temp=False
            break
    if temp:
        print(num,"is a prime number")
    else:
        print(num,"is not a prime number")