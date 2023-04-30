mymoney = 1000 
name = "saghar" 
lastname = "abazri"


user = input(f"Hello {name} {lastname} , how much is your account balance?  ")
userbuy = input("What do you like to buy?")
price = float(input("How much is it? "))
user_need = float(input("How much do you need?"))





a = price * user_need 
total = mymoney 
user_balance = float(a - total)
print("you spent:" , a , "and your balance now is: " , user_balance)
print("thank you for choesing us ! ")
