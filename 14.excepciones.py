## Error in execution time


def div(num, num2):

    try:
        return num / num2
    except ZeroDivisionError:
        print("Divisor can not be zero")
        return "Operator error"


print("This is a divisor app")

while True:
    try:
        numerator=int(input("Please enter your numerator \n"))
        divisor= int(input("Enter the divisor \n"))

        break    

    except ValueError:
        print("Values must be numerical")

print("Result is: " + str(div(numerator, divisor)))    