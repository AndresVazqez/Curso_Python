## Polymorphism

class Car():
    
    def moving(self):
        print("I am moving in car")


class Moto():

    def moving(self):
        print("I am moving in moto")


class Truck():

    def moving(self):
        print("I am moving in truck")


def movinVehicle(vehicle):
    vehicle.moving()


myVehicle = Moto()
myVehicle.moving()

myVehicle2 = Car()
myVehicle2.moving()

myVehicle3 = Truck()
myVehicle3.moving()

movinVehicle(myVehicle)