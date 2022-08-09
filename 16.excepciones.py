import math

## Exceptiones with raise, Luego dle raise no se ejecutan el resto de las lineas. 

def evaluate(age):
    if age <= 0:
        raise TypeError("Cannot be less than 0")
    elif age < 20:
       return  "You are to young"
    elif age < 65:
        return "You are a adult"
    elif age < 100:
        return "Be careful"
    else:
        return "Cannot be more than 100"


result = evaluate(10)

print("Functon 1: "+ "-------------------------" + result)


def pow(num):

    if num < 0:
        raise ValueError("number cannot be less than 0") 
    else:
        return math.sqrt(num)

## Debemos tener try and exepcion para poder continuar con la ejecución

try:
    print("Function 2: --------------------------------- " + str(pow(16)))
except ValueError as ErrorNegativeNum:
    print(ErrorNegativeNum) 

print("App is finished")