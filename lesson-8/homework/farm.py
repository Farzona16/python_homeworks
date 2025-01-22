class Animal:
    def __init__(self,name,age,weight):
        self.name=name
        self.age=age
        self.weight=weight

    def eat(self):
            print(f"{self.name}  is eating now")

    def sleep(self):
            print(f"{self.name} is sleeping now")

class Cow(Animal):
    def moo(self):
        print(f"{self.name}`s voice is 'moo'")

class Chicken(Animal):
    def cluck(self):
        print(f"{self.name}`s voice is 'cluck'")

class Dog(Animal):
    def bark(self):
        print(f"{self.name}`s voice is 'bow-wow'")
cow=Cow('Cow', 3, 300)
chick=Chicken('Chicken',1,2)
dog=Dog('Rokki', 3 ,50)

cow.eat()
cow.moo()
cow.sleep()
chick.eat()
chick.cluck()
dog.sleep()
dog.bark()