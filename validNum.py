while True:
    try:
        n=int(input("Enter a number: "))
        if n>0:
            print(f"{n} is valid ")
            break
        else:
            print("Enter a positive integer")
    except:
        print("Invalid input")