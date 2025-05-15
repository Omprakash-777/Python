def power(x, y):
  
    if y == 0:
        return 1
    
    if y < 0:
        return 1 / power(x, -y)
    
    return x * power(x, y - 1)


x = int(input("Enter the base no. : "))
y = int(input("Enter the exponent No. : "))

print(f"{x}^{y} = {power(x, y)}")
