frutas=['limon', "naranja", "pera"]
masFrutas=["kiwi", "mango", "sandia"]

##print all arrays
print(frutas)

## print last element in array
print(frutas[-1])

## print second element in array
print(frutas[1])

print(frutas.index("limon"))

## part of array list
print(frutas[0:2])

## add element in list
frutas.append("manzana")
print(frutas[:])

## add element in position 
frutas.insert(1, "platano")
print(frutas)

## add other array to array 
frutas.extend(masFrutas)
print(frutas)

## if element is in array return true o false
print("kiwi" in frutas)

## array with various data of type 
arrayMix  = ["Andres", 31, True]
print(arrayMix)

## delete elemtn in array
frutas.remove("sandia")
print(frutas)

## delete the last element in array
arrayMix.pop()
print(arrayMix)

## add array to array
arrayAll= frutas+arrayMix
print(arrayAll) 

## repeat list
frutasX3= frutas * 3
print(frutasX3)
