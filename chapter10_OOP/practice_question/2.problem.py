# 2. Write a class “Calculator” capable of finding square, cube and square root of a number
class calc:
    def __init__(self,n):
        self.n = n;
    
    def square(self):
        print(f"The Square is {self.n*self.n}")
    
    def cube(self):
        print(f"The cube is {self.n*self.n*self.n}")
    
    def sqrt(self):
        print(f"The Square root is {self.n**1/2}")
    
a = calc(4)
a.square()
a.cube()
a.sqrt()