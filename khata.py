#ijade khata mikonim khodemon 

#age = int(input("how old are you?\n"))
#if age < 18:
    #raise Exception("this is a error...")







# number = int(input("enter number:"))#-1,0,1 meghdar sahih
# if number < 0:
#     raise Exception("please enter a positive number...")




# x = []
# for i in range(5):
#     print("number(",i,"):")
#     num = int(input("please enter a number: "))
#     x.append(i)
#     if num  < 0:
#         raise Exception("please enter a positive number...")
#     else:
#         print("thats great!")
#         print(x)

# try:
#      num = int(input("please enter a number: "))
     
# except Exception as a:
#     print(a)





#number mosbat mikhaym

# def income(number):
#     if number < 0:
#         raise Exception("Please enter a positive number...")
#     else:
#         print("thank you :)")



# try: 
#    number = int(input("please enter a number: "))
#    income(number)
# except ValueError:
#     print("error")
# except Exception as e:
#     print(e)






#ijad khata hamrah ba takid !!!
'''
ye tafavot ke beine Exeption va assert hast inke Exeption mitone hame khataha ro dar bar begire ama assert faghat ye kar mitone kone masalan ma goftim zire sefr age number vared kardim error bede pas faghgta hamin ro error mide age horof vared konim chan klhat error mide mese hame error ha 
'''



# def income(number):
#     assert number >= 0,'you have error...'



# try:   
#     number = int(input("please enter a number: "))
#     income(number)
# except AssertionError as b:
#     print(b)




#age under 18 sal bashe error bede 

# def age(age):
#     if age < 18:
#         raise Exception("you are under 18 years old !!!!")


# try:
#     x = int(input("please enter your age : "))
#     age(x)
# except ValueError:
#     print("you need enter a number !!!")
# except Exception as a:
#     print(a)




# inbar ba assert neveshtim hamon cod ebala ro
def age(age):
    assert age >= 18,'you are under a 18 yeras old!!!'
    
try:
    x = int(input("please enter your age: "))
    age(x)
except ValueError:
    print("please enter a number !!!")
except AssertionError as b:
    print(b)