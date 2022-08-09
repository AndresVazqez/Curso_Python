## Function super() call method of parent class. isinstance()
## Principio de sustitucion es la regla de "Es un" un empleado es una persona.
class Person():
    
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def description(self):
        print("Name: " + self.name  + "\n" 
        + "Age: " + str(self.age) + "\n" 
        + "City: " + self.city )

class Employee(Person):                            

    def __init__(self, salary, seniority, name, age, city):

        super().__init__(name, age, city)

        self.salary = salary
        self.seniority = seniority

    def description(self):
        super().description()
        print("Salary: " + str(self.salary) + "\n"
        + "Seniority: " + str(self.seniority))
     

andres = Employee(22000, 1, "Andres", 32, "Madrid")

andres.description()

print(isinstance(andres, Person))