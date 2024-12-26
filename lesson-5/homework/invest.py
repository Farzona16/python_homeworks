def invest(amount,rate,years):
    for year in range(1, years+1):
        amount=(1+rate)*amount
        print(f"in {year} year: {amount:.2f} usd ")
try:
    a=float(input("enter the principal amount: "))
    r=float(input("enter the annual rate: "))
    y=int(input("enter the number of years which you need: "))
    invest(a,r,y)
except ValueError:
    print("Invalid input! Please enter numeric values.")

        