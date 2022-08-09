## String Methods 

texto = input("Enter some text!  \n")

##print(texto.upper())
##print(texto.lower())
##print(texto.isdigit())  ## True or False

while(not texto.isdigit()):

    print("Enter your age. \n")
    texto = input()

if (int(texto) >= 18 ):
    print("You are a adult!")
else:
    print("You are too young!")