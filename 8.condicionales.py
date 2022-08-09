## scholarship program

distance = 30
brothers = 2
family_salary = 15000

if (distance >= 40 and brothers >= 4) or family_salary <= 40000:
    print("You can obtain the scholarships")
else :
    print("Yo dont need the scholarships")


### Operator in

subjectList = ["math", "biology", "religion", "chemestry", "physics" ]

subject = str(input("Please insert the subject \n")).lower()


print("Input value :" + subject)

if subject in subjectList :
    print("The subject is ok")
else :
    print("Invalid subject")