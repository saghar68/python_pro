#parent
class Person:
    def __init__(self,fname,lname,age):
        self.fname=fname
        self.lname=lname
        self.age=age
    def fullname(self):
        print(f"{self.fname}{self.lname}")

#child 
class Student(Person):
    def __init__(self,fname,lname,age,Class,year):
        Person.__init__(self,fname,lname,age)
        self.Class=Class
        self.year=year
    def about_student(self):
        text =f'name:{self.fname}{self.lname}\nage:{self.age}\nclass:{self.Class}\nyear:{self.year}'
        return text
    
    
class Teacher(Person):
    def __init__(self, fname, lname, age,work,money):
        super().__init__(fname, lname, age)
        self.work=work
        self.money=money
    def about_teacher(self):
        print(f'name: {self.fname} {self.lname} working at school and\n {self.fname} is {self.work}\n and every month he get {self.money} pound.')

    
        
a=Student("saghar","abazari",14,5,1400)  
a.fullname() 
print(a.about_student())
b= Teacher("ali","hajipour",40,"Teacher",2000)
b.about_teacher()






        
# p = Person("ali","abazari",14)
# p2 = Person("sara","hajipour",40)
# p.fullname()


