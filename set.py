# test = {"sara",4,"amin","sara",2,4} #set ah mavared tekrari gheireghabele ghabole 
# print(test)
# print(len(test))#len ham mavarede tekrari ro nemishmare toye set 
# print(type(test))






from turtle import clear


t = [3,8,4,3,8]
x = list(set(t)) #hazf adadd tekrari dar list ba komake set
print(x)




#dar set har bar ke print migiri taghir mikone , jaygah dark nemishe va yek sare random jaygozini mishe 
#ma dar set na mitonim index begirim va slicing 


#methode haye set 

colors = {"red","yellow","pink","orange"}
color2 = {"green","brown","gray","red"}
#colors.add("blue")
#colors.remove("red")
colors.update(color2) #dar update mitonim az tuple va list ham estefade konim
#colors.remove("pink")

colors.discard("Pink") #hamon kare remove ro anjam mide ba in tafavot ke agar to yadet bere ke folan gozine ro pak kardi dg beeh error neshon nemide 
x = colors.pop()#random pak mikone pop dar test 
print(x)
print(colors)

del colors #vaghti az del estefade mikonim kolan pak mikone va error mide yani hamchin chizi nis

print(colors)

# colors.clear()
# print(colors)

