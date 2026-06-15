class Employee:
    language = "Python";
    salary = 120000;
    
    def __init__(self):
        print("Hello , Here is your information")
    
    @staticmethod
    def greet():
        print("Good morning")
        
    def info(self):
        print(f"The language is {self.language} and the salary is (self.salary)")
        
Employee.greet()
harry = Employee()
harry.name = "Harry"
print(harry.name , harry.salary)

Radhe = Employee()
Radhe.name = "Radhe"
print(Radhe.name , Radhe.language, Radhe.salary )

