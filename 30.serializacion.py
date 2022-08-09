## método dump() nos permite un volcado de datos al fichero binario externo.
## método load() carga los datos del fichero binario externo.

import pickle

names = ["Andrés", "María", "Juan", "Pedro"]

ficheroBinario = open("Fichero_Binario", "wb")

## two arguments; info to save, file name to save
pickle.dump(names, ficheroBinario)

ficheroBinario.close()

fileToRead = open("Fichero_Binario", "rb")

names2 = pickle.load(fileToRead)

print(names2)