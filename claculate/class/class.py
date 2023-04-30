#class 
#mesle str, int,list

class Car:
    def __init__(self,color,name):
        self.color=color
        self.name=name
        self.wheels=4
    def test(self):
        print("*" * 15)
        print(f"my car name is: {self.name}\nand my car color is: {self.color}")
        print("*" * 15)
    def about_wheels(self):
        ###wheels = int(input("how many wheels is on your car ? "))
        ##print(f"{self.name} have {self.wheels} wheels.")
        #print("*" * 15)
        print(f"{self.name} have {self.wheels} wheels.")

x1 = Car("red","Bmw")
x2 = Car("blue","benz")
x3 = Car("pink","pars")
#x3.wheels=3 #meghdar ro inja taghir dadim 
#del x3.wheels #bara pak kardan joz joze bara kol ham az del x2 use kon 
x3.about_wheels()
###


