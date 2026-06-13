class Employee:
    salary = 120000
    language = "Python"

    def getinfo(self):
        print(f"The language is {self.language} . The salary is {self.salary} ")
    
    def greet(self):
        print("Good morning") 
    

harry = Employee()
harry.language = "Javascript"
harry.getinfo()
harry.getinfo()


# self = the current instance object
#"We use self as a parameter that accepts the instance value."
