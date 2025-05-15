n=int(input("Enter the no.: "))
num = 1

c = 1  
for i in range(num, n+1):
    for j in range(c):
        if num > n:
            break
        print(num, end=" ")
        num += 1
    print()
    c += 1  