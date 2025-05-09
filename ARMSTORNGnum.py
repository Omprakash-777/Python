num = int(input("Enter a number: "))
original = num
num_digits = len(str(num)) 
sum_of_powers = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum_of_powers += digit ** num_digits
    temp = temp // 10
if sum_of_powers == original:
    print(original, "is an Armstrong number")
else:
    print(original, "is not an Armstrong number")