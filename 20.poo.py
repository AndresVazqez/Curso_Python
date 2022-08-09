## class inheritance
class Employee():
    name = "Andres"
    lastname = "Vazquez"
    age = 31

    def __init__(self):
        self.name = "Pedro"
        self.lastname = "Vazquez"
        self.age = 36   

## Other class
class Owner():
    def owner(self):
        print("Shut up, i am the owner")


## inheritance and multi inheritance
class Boss(Employee, Owner):
    def joder(self):
        print("Joder function")


myBoss = Boss()

## Employee method 
myBoss.joder()

## Owner method
myBoss.owner()

print(myBoss.name)


