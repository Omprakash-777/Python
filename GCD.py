def gcd(x, y):
    if y==0:
        return x
    return gcd(y, x%y)

# Input from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print(f"The GCD of {num1} and {num2} is {gcd(num1, num2)}.")
