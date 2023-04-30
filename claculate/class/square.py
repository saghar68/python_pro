



class square:
    def __init__(self,a):
        self.a=a
        
    def area(self): #masahat daiere ye zel * khodesh
        print(f"this is area square:\n{self.a}x{self.a}={self.a*self.a}")
    def mohit(self):#4 zarbedar zel
        print(f"this is mohit square\n4x{self.a}={4*self.a}:")
    def square(self):
        print(f"{self.a}x0.5={self.a*0.5}")

    


a = int(input("enter a number: ")) 
x=square(a)      
x.area()
x.mohit()
x.square()