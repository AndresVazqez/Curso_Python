## generators creamos un objeto generador iterable.

## Normal function

def generatorOven(limit):

    list=[]
    num=0

    while num < limit:
        num += 2
        list.append(num)
    return list


print(generatorOven(60))


## Generator

def generatorOven2(limit):

    num=2

    while num < limit:                     
        num +=2
        yield num

    

# generator = generatorOven2(10)

# ## with loop for
# for i in generator:
#     print(i)

generator = generatorOven2(100)

## With next method
## Se guarda el generador de numero en la variable y va generando numeros cada vez que es llamada la funcion (generador)
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
