class Employee:
    language = "Python";
    salary = 120000;
    
    def __init__(self,name,language,salary):  #here we don
        self.salary = salary
        self.name = name
        self.language = language
        print("Hello , Here is your information")
    
    @staticmethod
    def greet():
        print("Good morning")
        
    def info(self):
        print(f"The language is {self.language} and the salary is (self.salary)")
        
Employee.greet()
harry = Employee("Harry" , "Python" , 50000)
print(harry.name ,harry.language , harry.salary)

Radhe = Employee("Kanha","c",900000)
print(Radhe.name , Radhe.language, Radhe.salary )

