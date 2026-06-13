class Employee:
    salary = 120000
    language = "Python"
    

harry = Employee()
harry.language = "Javasript"  #Note: Instance attributes, take preference over class attributes during assignment & retrieval. 
print(harry.language, harry.salary )