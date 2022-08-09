## loops
frutas = ["Pera", "manzana", "mango", "naranja"] 

for fruta in ["Pera", "manzana", "mango", "naranja"] :
    print(fruta)

print("----------------------------------------------------------")

for fruta in frutas:
        print(fruta)

string = input("Please, enter your email \n")

validEmail = False
validDot = False
string = string.lower()

for character in string:
    if character == '@':
        validEmail = True
    elif character == '.' :
        validDot = True
 
if validEmail and validDot :
    print("The email is valid")
else :
    print("Invalid email")
print("---------------------------------------------------------------")

## use range 
for i in range(len(frutas)):

    print("Position " + str(i) + " is " + frutas[i])
    print(f"Position {i} is {frutas[i]}")

print("---------------------- Range --------------------")

## for with determinated range
for i in range(1,10,2):
    print(i)
