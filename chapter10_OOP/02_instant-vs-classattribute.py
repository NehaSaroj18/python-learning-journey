class Employee:
    salary = 120000
    language = "Python" # this is class attribute
    

harry = Employee()
harry.language = "Javasript"  # this is instant attribute 
print(harry.language, harry.salary )


#Note: Instance attributes, take preference over class attributes during assignment & retrieval. 
