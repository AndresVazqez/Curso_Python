## the tuplas are a inmutable lists

from typing import List


tupla=("rojo", "negro", "blanco", "azul", 31, 55, "rojo")
print(type(tupla))
print(tupla)

## print index 4 in the tuple
print(tupla[4])
print(tupla.index("rojo"))

## verify element in tuple
print(31 in tupla)

## convert tuple in array 
myArray=list(tupla)
print(type(myArray))
print(myArray)

myTuple= tuple(myArray)
print(type(myTuple))

## count element in array o tuple
print(myTuple.count("rojo"))

## arrays or tuple length
print(len(tupla))
print(len(myArray))

## unitary tuple
myUnitTuple= ("Andres", )
print(myUnitTuple)
print(len(myUnitTuple))

## destructuring array or tuple
cars=["leon", "A1", "corolla"]
seat, audi, toyota = cars
print(seat)