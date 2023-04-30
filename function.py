#function

#tamame tabeha makhsose ye amaale khase mesle 
#type, len, sum 


# def sayhello(name):
#     print("hi",name)
    
# #sayhello("saghar")
# for i in range(2):
#     name = input("whats your name?")
#     sayhello(name)


# #pass 

# if 6 > 2 :
#     pass
# else: #vaghti nemidonim ye ghesmat az code ro kamel konim az pass estefade mikonim 
#     pass
   
# name = input("whats your name")
 
 
 
# #return

# def welcome(name):
#     return f'welcome to my site {name}'  

# name = input("whats your name? ")
# print(welcome(name).upper()) #vaghti az return estefade mikonim mitonim az method ha estefade konim dar print vaghti az return estefade mikjonim mitonim aaniii ye chi ro taghir bedim mesle in mesal



#docstring 

#doc string = ''' ''' , """ """ 
#bara comment tolani va dar chan khet neshon mide 
# dar def mitonim az docstring estefade konim bishtar dar tavabe va class ha use mishe 


# def welcome(name):
#     '''with this function we say welcome to every one '''

# print(welcome.__doc__)



#default 


# def about_user(name,family,age=13,From="iran"):
#     print(f"name: {name}\nfamily: {family}\nage: {age}\nFrom: {From}\n")
    

# about_user("ali","alizade")
# about_user("saghar","abazari",34)
# about_user("amir","abazari")




#ye ravesh dg

# def get_age():
#     age = int(input("how old are you? "))
#     print(f"i am {age} years old")


# for i in range(5):
#     get_age()
    
    

# def func(n):
#     return n**5

# print(func(9))
  
  
              
 
#halghe zadan dar def 

# def test(name_list):
#     for i in name_list:
#         print(i) 

# name =["ali","reza","mina"]
# test(name)  

def test(name_list):
    for i in name_list:
        print(i)
        
name = ["ali","mina","nima","amin"]
test(name)










#args

# def test(*args): #in *in kheili moheme, ma vaghti parametr ziad darim mitonim az args estefade konim 
#     print("the name",args[4])
    
# test("ali","reza","mina","sara","alireza")#vaghti az *args estefade konim ta har chanta bekhaym mitonim inja benevisim , azadim 



# #ye mesale dg az *args

def test(*args):
    result = 0
    for i in args:
        result += i
    return result
    
print(test(8,9,56,78,67,89))
    





#**kwargs ye dic dorost mikone 

# def test(**kwargs):
#     print(kwargs)

# test(name="saghar",family="abazari",age=34,From="Iran")