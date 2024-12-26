def is_prime():
    a=int(input("Enter the prime number: "))
    if a>1:
        for i in range(2,a):
            if a%i==0:
                print(False)
                break
        else:
            print(True)
    else:
        print("Please enter correct number!")
is_prime()