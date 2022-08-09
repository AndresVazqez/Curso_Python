## several exceptions in a function, try must have a except or finally

def div():

    try:

        numerator = float(input("Enter numerator: \n"))
        divider  = float(input("Enter divider: \n"))
        print("The result is: " + str(numerator/divider))


    except ValueError:

        print("Value must be numerical")

    except ZeroDivisionError:

        print('divider can not be zero "0" ')
    
    ## finally:  se ejecuta si o si, aunque falle algo. 
    ##finally:
    
div()

## General exceptions

def div2():

    try:
        numerator = float(input("Enter numerator: \n"))
        divider  = float(input("Enter divider: \n"))

        print("The result is: " + str(numerator/divider))

    except:
        print("Something went wrong")