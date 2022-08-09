from audioop import add
from io import open

## for read and write file r+
archivo=open("fichero.txt","r+")

## Read from especific position
archivo.seek(10)
text=archivo.read()
print(text)

archivo.seek(0)

## Read from this position
text=archivo.read(3)

archivo.close()

print(text)

print("--------------------------__________________----------------------------")

archivo= open("fichero.txt", "r+")

text = archivo.read()
print("Texto en el fichero: ")
print(text)

addText="\nTexto agregado"
archivo.write(addText)

print("Text after add text")
print(text)

## File in lists
print("----------------------------- texto en lineas ------------------------ ")

archivo.seek(0)
textlines = archivo.readlines()

print(textlines)
print(textlines[2])
