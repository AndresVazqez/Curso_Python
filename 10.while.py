## loop while
num = 1
vuelta = 1
while num <=10:
    print("Vuelta : " + str(vuelta))
    vuelta = vuelta + 1
    num = num + 1     


### Indeterminate loop
age = int(input("Please insert your age \n"))

while age < 0 or age > 100:
    print("Invalid age")
    age = int(input("Please insert your age \n"))

print("Your age is: " + str(age))

### Logics Operators with indeterminate loop 
choice = int(input("Please choose a option: \n 1. si \n 2. no \n 3. nose"))

while choice != 1 and choice !=2 and choice != 3:
    choice = int(input("Please choose a option: \n 1. si \n 2. no \n 3. nose"))

print("well donde, your choice is: " + str(choice))

