def factor():
    n=int(input("Enter the positive integer number: "))
    if n<=0:
        print("Please enter the correct number!")
    else:
        for i in range(1,n+1):
            if n%i==0:
                print(f"{i} is factor of {n}")
factor()