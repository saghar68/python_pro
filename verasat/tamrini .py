class Parent():
    def __init__(self,name,age,job,time,adress):
        self.name=name
        self.age=age
        self.job=job
        self.time=time
        self.adress=adress
    def fullnames(self):
        print("*"*30)
        print("your welcome to our website.")

class Doctor(Parent):
    def __init__(self,name,age,job,time,adress,heart):
        super().__init__(name,age,job,time,adress)
        self.heart=heart
    def Person1(self):
        text=f"my name is {self.name} \nim {self.age} years old\nim a {self.job}\nyou can meet me every day at {self.time} o'clock\nim working at {self.adress}\nmy takhasos is {self.heart}"
        print("*"*30)
        return text
    def Person2(self):
        text1=f"my name is {self.name} \nim {self.age} years old\nim a {self.job}\nyou can meet me every day at {self.time} o'oclocks\nim working at {self.adress}\nmy takhasos is {self.heart}"
        print("*"*30)
        return text1
    
       


d1 = Doctor("Saghar Abazari",32,"DOCTOR",12,"newcastel Hospital","Heart Surgury")
d1.fullnames()
print(d1.Person1())
d2 = Doctor("Amin Hajipour",44,"Doctor",2,"Stock Hospital","child and baby's")
print(d2.Person2())


