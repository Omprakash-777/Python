n,m=map(int,input("Enter the Row and Column separted by space: ").split())
num=1
for i in range(1,n+1):
    for j in range(1,m+1):
        if i==1 or j==1 or j==m or i==n:
            print(num, end=" ") 
            num+=1
        else:
            print("0", end=" ")
            num+=1
    print()
    