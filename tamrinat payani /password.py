#make a password 


import random 


t = 1
while t != 0:
    carbar =int(input("enter the lenght of password:\n"))
    s = "mnbvcxzlkjhfgfdsapoiuytrewq0987654321}"
    p = "".join(random.sample(s,carbar))
    print(p)


