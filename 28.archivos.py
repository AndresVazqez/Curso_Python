### Extenal files

from io import open

## Open and write in file
archivo1=open("fichero.txt","w" )

frase="Esto es una fraseeeeeee! \nSegunda linea \nTercera linea"

archivo1.write(frase)

## close file in memory
archivo1.close()

## Only read open
archivo=open("fichero.txt", "r")

## Save in variable the text file
## Read or readlines
textLines=archivo.readlines()

## Return position 0 after firts read
archivo.seek(0)

texto=archivo.read()
archivo.close()

print("(" + texto + ")")
print("------------------ tex lines --------------------")
print(textLines)

archivo=open("fichero.txt", "a")

archivo.write("\nLinea agregada con open")

archivo.close()

