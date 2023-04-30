#ye ebarname ghore keshi 
#10 ta email daryaft kone 
#dakheili ye file bendaze vasateshon yeki ro barande beshe 


emails = []
for i in range(1,11):
    carbar= input("please enter email:")+"\n"
    emails.append(carbar)


file = open("text.txt","w")
file.writelines(emails)
file.close()
file = open('text.txt',"r")
print(file.read())
    






#10 ta kalame 5 harfi payda konm va chap konm 

# import random


# with open("text2.txt","r") as file:
#     x = file.read().split()
#     x = [i for i in x if len(i)==5]
#     print(x)
# for i in range(6):
#     print(random.choice(i))
    

