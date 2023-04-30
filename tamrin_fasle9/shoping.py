# def show(mylist):
#      print("the item is in your shopping list :)")
#      for i in mylist:
#         print(f"{i}")
  
  
    
# def search(mylist,item):
#     if item in mylist:
#         print(f"yes, this {item} in your shopping list")
#     else:
#         print(f"No, this {item} its not in your shopping list!")


# def delete(mylist,item):
#     if item not in mylist:
#         print("this item not in your list shopping! sorry")
#     else:
#         mylist.remove(item)
#         return mylist  




# shoping =[]
# item_number=int(input("enter your item you want to add the list please:\n"))

# for i in range(1,item_number+1):
#     item = input("enter your items:\n").title()
#     shoping.append(item)

# t = 1
# while t != 0:
#     print("-----------------------------------------")
#     print("menu shop app:") 
#     print("1.show all\n2.search item\n3.delete item\n0.close") 
#     t = int(input("enter your choese:\n "))
#     print("-------------------------------------------")
#     if t == 1:
#        show(shoping)
#     elif t == 2:
#         item = input("enter your items:\n").title()
#         search(shoping,item)
#     elif t == 3:
#        print(shoping)
#        item = input("enter your items:\n").title()
#        delete(shoping,item)




def show(mylist):
    print("the item in your basket is: ")
    for i in mylist:
        print(f"{i}")

def search(mylist,item):
    if item in mylist:
        print(F"yes , you add {item} in your basket")
    else:
        print("No, you didnt add any item in your basket")


def delete(mylist,item):
    if item not in mylist:
        print("we cant find any item in your basket ! sorry...")
    else:
        mylist.remove(item)
        return mylist


    

shoping = []
list_number = int(input("How many item do you want to buy: "))

for i in range(1,list_number+1):
    item = input("enter your item name please: ").title()
    shoping.append(item)
    print(shoping)
    
t = 1

while t != 0:
    print("<-*-*_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_*-*->")
    print("MENU SHOP: ")
    print("1.show all\n2.search item\n3.delete item\nclose")
    carbar = int(input("please enter your number choose: "))
    
    if carbar == 1:
        show(shoping)
    elif carbar == 2:
        item = input("enter your items: ")
        search(shoping,item)
    elif carbar == 3:
        item = input("enter your items: ")
        delete(shoping,item)