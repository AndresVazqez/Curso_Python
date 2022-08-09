    ###################################################
   # ----------------------------------------------- #
  # ----------- hace lo que quiere----------------- #
 ###################################################


## Encapsular los atributos colacando dos __ antes. ej. __large

class Cars2():
    __large = 300
    __weigth = 150
    __wheels = 4
    __moving = False


    ## Constructor 
    def __init__(self, large, weight, wheels, moving):
        self.__large = large
        self.__weigth = weight
        self.__wheels = wheels
        self.__moving = moving

    def toString(self):
        print("Large: " + str(self.__large) + "\n"
        + "Weight : " + str(self.__weigth) + "\n"
        + "Wheels: " + str(self.__wheels) + "\n"
        + "Moving: " + str(self.__moving))

myCar = Cars2(400, 200, 3, True)

print("--------------------------------------------")

# print("Large 1:--------- " + str(myCar.__large))

myCar.__large = 800

print("Large 2:--------- " + str(myCar.__large))

myCar.toString()

print("Large 3:--------- " + str(myCar.__large))
