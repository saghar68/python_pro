def calcu():
    num1 = float(input("please enter your number:\n"))
    num2 = float(input("Please enter your number:\n"))
    ope = input("Please enter operator:\n1.for add +\n1.for sub -\n3.for multi *\nfor divs /\n"   )
    if ope == "+":
        add = num1 + num2
        print("{}+{}={}".format(num1,num2,add))
    elif ope == "-":
        sub = num1 - num2
        print("{}-{}={}".format(num1,num2,sub))
    elif ope == "*":
        multi = num1 * num2
        print("{}*{}={}".format(num1,num2,multi))
    elif ope == "/":
        divs = num1 / num2
        print("{}/{}={}".format(num1,num2,divs))
    else:
        print("somthing wrong! plz try again...")
        
    again()
        
        
def again():
    c = input("Do you want try again(yes/no)?\n")
    if c == "yes":
        calcu()
    elif c == "no":
        print("thank you for choosing us :)")
    else:
        again()
      
    
    
calcu() 







