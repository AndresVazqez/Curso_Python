## Programing oriented Object

class Cars():
    large = 300
    weigth = 150
    wehels = 4
    moving = False

    def start(self):
        self.moving = True

    def status(self):
        if (self.start):
            return "The car is moving"
        else:
            return "The car is stop"
    
    def saluda(self, name):       
        return "Hi, : " + name

myCars = Cars()

print(myCars.saluda("Andres"))
print(myCars.large)
print(myCars.status())

