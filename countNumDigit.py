num = int(input("Enter a number: "))
temp = 0
if num == 0:
    temp = 1
else:
    while num > 0:
        num //= 10
        temp += 1
print("Number of digits:", temp)