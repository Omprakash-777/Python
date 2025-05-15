def GCD(a, b):
    while b:
        a, b = b, a % b
    return a

n1, n2 = map(int, input("Enter the two numbers separated by space: ").split())
lcm = abs(n1 * n2) / GCD(n1, n2)
print(f"LCM of {n1} and {n2}: {lcm}")
