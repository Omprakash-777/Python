a=float(input("Enter first number: "))
b=float(input("Enter second number: "))

operator=input("Enter operation: ")

if operator == '+':
    print(a+b)
elif operator == '-':
    print(a-b)
elif operator == '*':
    print(a*b)
elif operator == '/':
    if b != 0:
        print(a/b)
    else:
        print("Invalid input")