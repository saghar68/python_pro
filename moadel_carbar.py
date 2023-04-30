numbers = []
count = int(input("please enter your numbers:\n"))


for i in range(1,4):
   numbers.append(input("please enter number:"+ str(i+1)+"\n"))

print(numbers)

for x in reversed(numbers):#vaghti az methode reveres estefade mishe az akhar neshon mide shomareharo
   print(x)