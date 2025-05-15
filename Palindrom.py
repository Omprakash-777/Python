n=int(input("Enter the number: "))
ori=n
rev=0
while(n>0):
    digit=n%10
    rev= rev*10+digit
    n//=10
if(ori==rev):
    print("Palindrom")
else:
    print("Not Palindrom")
