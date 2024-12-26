def convert_far_to_cel():
    F=float(input("enter the temperature in Fahrenheit(F): "))
    C=(F-32)*5/9
    print(f"{C:.2f}")
convert_far_to_cel()

def convert_cel_to_far():
    C=float(input("enter the temperature in Celcium(C): "))
    F=C*9/5+32
    print(f"{F:.2f}")
convert_cel_to_far()
