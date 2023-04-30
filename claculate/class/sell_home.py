# class House:
#     def __init__(self,color,num_of_room,a):
#         self.color=color
#         self.num_of_room=num_of_room
#         self.a=a
        
        
#     def description(self):
#         print(f"House color:{self.color}\nNumber of room this house:{self.num_of_room}\nmasahat of this house:{self.a}")
#     def rent(self):
#         carbar = int(input("enter your rent: "))
#         print(f"the rent of this House is £{carbar*self.a}")
#     def buy(self):
#         buy_home= int(input("enter buy home: "))
#         print(f"you need pay for buy this home is:{5000*self.a} ")
        
        
        
           
       
        
        
        
# h = House("red",3,100)
# h.description()
# h.rent()
# h.buy()    
        
   
   


#ye modele dg 

class House:
    country="iran"
    def __init__(self,color,num_of_room,a):
        self.color=color
        self.num_of_room=num_of_room
        self.a=a
        
        
    def description(self):
        print(f"House color:{self.color}\nNumber of room this house:{self.num_of_room}\nmasahat of this house:{self.a} metr\ncountry: {self.country}")
    def rent(self):
        #carbar = int(input("enter your rent: "))
        print(f"the rent of this House is £{carbar*self.a}")
    def buy(self):
        #buy_home= int(input("enter buy home: "))
        print(f"you need pay for buy this home is:{5000*self.a} ")
        
        
        
           
       
h = House("red",3,100)
del h.country #bekhaym yeki ro pak konim intor pak mikonim 






# #print(h.country)
# h.country="usa"
# print(h.country)
h.description()
# ##h.rent()
# #h.buy()    
        
            