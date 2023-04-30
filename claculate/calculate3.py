# def Calcu(num1,num2,ope):
#     if ope == "+":
#         result = num1 + num2
    
#     elif ope == "-":
#         result = num1 - num2
#     elif ope == "*":
#         result = num1 * num2
#     elif ope == "/":
#         result = num1 / num2
#     else:
#         result = "the operator is not found!"
#     print(result)
# try:
#     num1 = float(input("Please enter a number one:\n ")) 
#     num2 = float(input("Please enter a number two:\n"))
#     ope = input("Please enter a operator(+,-,*,/) \n")
# except:
#     print("something is wrong!")
# else:
#     Calcu(num1,num2,ope)           



def calcu(num1,num2,ope):
    if ope == "+":
        result = num1+num2
    elif ope == "-":
        result = num1-num2
    elif ope == "*":
        result = num1 * num2
    elif ope == "/":
        result = num1/num2
    else:
        result = "the operator not found!!!"
    print(result)
    print("thank you for choosing us")
try:
    num1 = float(input("Please enter your number one:\n"))
    num2 = float(input("Please enter your number two:\n"))
    ope = input("Please enter your operator (+,-,*,/)\n")
except:
    print("somthing is wrong")
else:
    calcu(num1,num2,ope)   


















   