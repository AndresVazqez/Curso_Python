## encapsulated method
class Vehicle():

    def __init__(self):
        self.__color = "blue"
        self.__motor = "V8"
        self.__brand = "Ford"


    def getBrand(self):
        print(self.__brand)

        self.__check()
        

    def setBrand(self,brand):
        self.__brand= brand
    
    ## encapsulated method
    def __check(self):
        print("Cheking in process")
        

myVehicle = Vehicle()

myVehicle.__brand= "Seat"

myVehicle.getBrand()

myVehicle.setBrand("Toyota")

myVehicle.getBrand()

