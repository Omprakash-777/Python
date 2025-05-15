n=int(input("Enter the number: "))
sum=0
l=len(str(n))
for i in range(l):
    sum+=n%10
    n//=10
print(f"Sum of the digit: {sum}")