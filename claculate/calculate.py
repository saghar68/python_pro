num1 = float(input("enter num1:\n"))
ope = input("enter(+, -, /, *,**)")
num2 = float(input("enter num2:\n"))


if ope == "+":
    x = num1 + num2
    print(x)
elif ope == "-":
    x = num1 - num2
    print(x)
elif ope == "/":
    x = num1 / num2
    print(x)
elif ope == "*":
    x = num1 * num2
    print(x)
elif ope == "**":
    x = num1 ** num2
    print(x)
else:
    print("somthing is wrong!")    
   