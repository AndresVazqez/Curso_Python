### Serialize object
import pickle

class Cars():
    large = 300
    weigth = 150
    wehels = 4
    moving = False

    def __init__(self, large, weigth, wehels, moving):
        self.large = large
        self.weigth = weigth
        self.wehels = wehels
        self.moving = moving

    def start(self):
        self.moving = True

    def status(self):
        if (self.start):
            return "The car is moving"
        else:
            return "The car is stop"
    
    def saluda(self, name):       
        return "Hi, : " + name

    def toString(self):
        print("Large: " + str( self.large) + 
        "\nWeigth: " + str(self.weigth) + 
        "\nWehels: " + str(self.wehels) +
        "\nMoving: " + str(self.moving))


myCars = Cars(400, 1300, 4, True)
myCars2 = Cars(500, 1400, 4, True)
myCars3 = Cars(600, 1500, 4, False)
myCars4 = Cars(700, 1600, 4, True)

cars = [myCars, myCars2, myCars3, myCars4]

fichero = open("Fichero_Binario", "wb")

pickle.dump(cars, fichero)

fichero.close()

fichero = open("Fichero_Binario", "rb")

dataBinary= pickle.load(fichero)

fichero.close()

i = 1
for car in dataBinary :
    print("Car " + str(i)+ ":")
    car.toString()
    i += 1
