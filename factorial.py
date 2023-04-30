#8!  intor neshon dade mishe 
#1*2*3*4*5*6*7*8 in yani factorial

#gereftane factorial az yrk adad



# num = int(input("please enter a number:\n"))

# f = 1
# if num < 0:
#     print(" Factorial it dosent work for negative numbers sorry!")
# elif num == 0:
#     print("the Factorial of 1 no 0")
# else:
#     for i in range(1,num+1):
#         f = f*i 
#         print("the Factorial of ", num,"is",f)
        
        
num = int(input("please enter your number :\n"))
f = 1
if num < 0:
    print("ziro it dosent factorial number,please try again!")
elif num == 0:
    print("you need enter diffrent number")
else:
    for i in range(1,num+1):
        f = f*i
        print("your factorial number", num ,"is",f)