## Conditionals

def evaluation (nota):

    result= ""

    if nota <= 9  : result = "Reprobate" 
    else : result = "Approved"
    
    return result

##scoreStudent = int(input("Please, insert the score \n"))

##print(evaluation(scoreStudent))


## Else with else if

age = input("Pleae, insert your age \n")


if str.isdigit(age):

    age = int(age)
    
    if age < 18 : 
        print("Eres menor de edad")
    elif age >= 18 and age <35  : 
        print("Eres mayor de edad y joven aún")
    elif age >= 35 and age < 120 :
        print("Ya estas mayor")
    elif age >= 120:
        print("You are a liar")  
else :
    print("error")
  