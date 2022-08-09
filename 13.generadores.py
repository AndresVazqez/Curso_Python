## Yield from 

cities1 = ["London", "Lisboa", "Madrid", "Barcelona"]

def cityReturn(*cities):
    for city in cities:
        yield city

citiesGenerator= cityReturn(cities1)

print(next(citiesGenerator))

print(next(citiesGenerator))
print(next(citiesGenerator))


###########################################################################
#                                                                         #
# ////////////////////////// NO FUNCIONA //////////////////////////////// #
#                                                                         #
###########################################################################