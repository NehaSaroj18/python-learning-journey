# 1. Create a class “Programmer” for storing information of few programmers 
# working at Microsoft. 

class programmer:
    comapny = "Microsoft"
    
    def __init__(self , name , salary , role, pincode):
        self.name = name
        self.salary = salary 
        self.role = role
        self.pincode =pincode
        
        print("Information of Employees working at Microsoft")
        
harry = programmer("Harry","Python Developer", 1200000,411027)
print(harry.name, harry.role,harry.salary,harry.pincode)


