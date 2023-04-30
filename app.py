#test =['mina', 'nima', 'nasim']

#for x in test:
    #print(f"hello {x}")
    
#test = "this is pythin class"

##for i in test:
    #print(i)
    


#range(start,stop,step)

#for i in range(1, 100,10):
    #print(i)
    
#####name = ['sara','nima','saghar', 'ayaan','anelly','arti']

####for i in name :
    ###print(i)
    ##if i == 'nima':
         #break
#ba in ravesh ta jaei ke mikhaym behemon neshon dade mishe  



#s = [0,4,8,98,43,9]

#for c in s :
    #print(c)
    #if not c <= 9:
     #break
     
     

#name = ['ali', 'sara', 'samira', 'tina', 'ali']

#for i in name:
    #print(i)
    #if len(i) == 6:
    #if "t" in i:
        #break
     
  
  
#continue



# name = ['ali', 'sara', 'samira', 'tina', 'tina', 'reza', 'omid']
#x = [i.title() for i in name if 'm' in i]
#print(x)

###z = [s for s in name  if lenmish ecode ()]


##for i in name:

   #if i == 'sara':
   #if 'm' in i:
        #continue
#print(i)
       
#discard #remove dar set 
#pop() ya ye chizi midi pak mikone ya az akhar pak mikone
 #add kardan dar set 
 #color = ["blue", "red"]
 #c = (12,3,5,5)
 #colors.update(c)
 #print(color)
  
#name=input("Please enter your name:\n")
#age=int(input("Please enter your age:\n"))
#weight=float(input("Please enter your weight:\n"))


#text="My name is %s I am %d years old and I am %.2f Kg!"%(name,age,weight) 
#print(text)  


#dar dics bara avaz kardan value az in ravesh estefade mikonim 

#user = {
    #"name": "ali"
    #"age": 12
#}

#user['age']= 14
#print(user['ago]) => vaghti eshteba benevisim dar dect
#print(user.get('nome', 'somting is wrong')) => minivise none yani eshteba kardi , mitonim peygham bezarim hata 
#print(user)
#bara add kardan ozve jadid 
#user.update({'email': ali2yahoo.com, 'phone': '0929383883}')







# user = {"name":"ali",
#         "email": 'saghi.abz@gmail.com',
#          'age' : 16,
        
#         }


#for i,j in user.items(): #faghat key ro neshon mide 
    #print(user[i])
    #print(f"{i}:{j}" )
    
#.values()
#.keys()
#bara ham key ham valuse az items() estefade mikonm  


# if ('name', 'ali') in user.items():
#     print("yes")
# else:
#     print("no")

#print(test[user2][live][life]) in bara dictionary to dictionary estefade mishe ke be kays beresim 





#zip()

# t1 = [12,3,34,5]
# t2 = ["a", "b"]

# print(list(zip(t1,t2)))


#mitonim set , tuble, list benevisim dar zip()

# name=["ali","mahshid","reza","mina"]
# age=(30,20,12,19)
# x={i.upper():j**2 for i , j in zip(name,age)if "m" in i and j%2==0}

# print(x)



#def 

#type, len, sum, print ina hame def hastan 






# def welcome(name):
#      print(f"welcome {name} ")

# for i in range(5):
#     name = input("please enter your name:\n")
#     welcome(name)



# def fullname():
#     """give name and last name"""
#     name = input("what is  your name?").strip()
#     lastname = input("what is your family?").strip()
#     print(f"{name.upper()} {lastname.title()}")
    
    
# fullname()
    



# s = lambda a,b,c : a*5 + (b*a) / (b/c) * a + b
# print(s(7,9,6))

# x = lambda a:a.replace("m","l")
# print(x("mina"))







#while 



# t = 0
# while t <= 10:
#     print(t)
#     t += 2
    
    

# i = 0
# while i < 15:
#     i +=1
#     if  i % 2==0:
#         continue
#     print(i) 
    

# while True:
#     name = input("enter your name:\n")
#     if name == 'stop':
#          break


# playe1 = input(" player one : enter your gusee:")
# try_count = 0
# x = False

# while try_count < 5 and x == False:
#     guess = int(input("please enter a number:"))
#     if guess == playe1:
#         print("You win")
#         x = True
#     elif guess > playe1:
#         print("youre guess is greater than answer")
#         try_count+=1
#     else :
#          print("your guess is smaller than answer ")
#          try_count+1
# if try_count == 5:
#     print("you lost")
    
 
 
    
#map, filtter 

#map(function,(list, tuple,set,dict))

# def a(b):
#     return b+2
#test = [9, 8, 3,6]
#x = list(map(lambda a:a/2, test))
#x = list(map(a,test))
#print(x)



# names = ["amir", "mina","reza","tina"]
# x = [i.replace('a','m') for i in names]
# print(x) >>>>> in ravesh mese ravesh paeeine, esmesh list for 



#x = map(lambda o:'m' in o,names)
#x = map(lambda t:t+ "hello" , names)
#x = map(lambda k:k.replace('m','ali'), names)
#print(list(x))

 #filtter
#filter(fun.(list<tuple,set))
 
# test = ["ali","reza","mina"]
# x = list(filter(lambda a:'m' in a, test))


#x = list(filter(lambda a:a.upper, test))
#x = list(map(lambda a:a.upper(), test))
# print(x)

# x = list(filter(lambda a:a['age']== 20,users))
# print(x)

# x =map(lambda b:b['name'], users)
# print(list(x))

# x = filter(lambda a:a['name'] == 'reza', users)
# print(list(x))

# x = map(lambda b:b['name']== 'reza',users)
# print(list(x))





# list = ["ali",
#         "sara", 
#         [1,2,3],
#         "arti",
#         "ayaan",
#         ["anelly","amin"]
#         ]

# print(type(list))
# print(list[2])
# print(list[0:6])
# print(len(list))


#text = ["sara","amin","anelly","ayaan"]
#x = "*".join(text)
#text[0] = "saghar"
#print(text+["reza"])
#text.append("arti")
#text.append(["a","b","c"])
#text.insert(1,"mina")
#text.extend(["ali","orang"]) #dar extend bayad hatman list vared koni , age faghat reshte vared koni tamam horof ro yeki yeki joda mikone
# text[1:2]=[3,4,5] #slising
# print(text)


#dar extand va append mitoni faghat ye ozve add koni ya ye list 




#ravesh hazf ye list 

#remove
#num = [78,98,2,3,4]
# num.remove(3)
# print(num)

#pop
#num.pop() #pop az akhar ye mored ro pak mikone vali ye halate dg ham kar mikone mishe shomare index behesh bedim chon suport mikone 
#num.pop(0) 
#print(num) 


#clear
# num.clear()
# print(num)


#delete

#del num #kamel pak mikone .va error neshon mide ye model dg mishe estefade kard 
#del num[2]


#slising

##num[1:4] = [] #az koja ta koja ro mishe pak kard tavasot slising
#print(num)



#index 

#x = ["a", "z","m","a","h","m"]

#print(x.index("m",3 ))
#count
#print(x.count("a"))
#x.reverse() #baraks chap mishe ba in 
#x.sort() #be tartib chap mikone , dar sort nemitoni ham string bezari ham adad faghat ye model mish eestefade kard 
#print(x)




#tuple 




#test = (23, 3, "sara", "ayaan", 3, 12,"arti")
#test[2] = "sima" #nemishe be rahati chizi add konim behesh in ravaesh error mikhore besh 

#print(test + ("sara","mina")) #ba in ravesh mishe add kard 


# print(len(test))
# print(type(test))
#print(test[2])
#print(test[1:3])
#test = test +("sara","mina") #bara add kardan tuple va list ba ham fargh daran 


#vaghti bekhaym ye taghir dar tuple dorost konim bayad on ro be ye list tabdil konim va bad az taghir dobare be tuple avaz beshe mesle mesal zir 

# test2 = list(test) 
# test2[3] = "amin"
# test = tuple(test2)
# print(test)


# test = (12,"ali","amin",23,"anelly",22)
# test2 = list(test)
# test2.insert(1,"amir") #ba in ravaesh bedon inke chizi hazf konim yeki ezafe kardim ba insert
# test = tuple(test2)
# print(test)


#hazf kardane ye tuple
# test = (12,"ali","amin",23,"anelly",22)
# test2 = list(test)
# test2.clear()
# test = tuple(test2)
# print(test)


#method haye ye tuple : 2 ta metode dare count va index
# test = (12,"ali","amin","ali","anelly",22)
# print(test.count("ali"))
# print(test.index("ali", 3)) #godtam ali avali na boro 3 be bad ro chek kon bebbin ali hast ?







#unpacking

# #ma dar unpaking vaghti * bezarim pishe moteghair ono bar migardone be list tabdil mikone 
# test = ("ali","alireza",12,2)
# (a,*b) = test
# print(a,b)


#for 

# colors = ["orange","blue","pink","red"]

# for color in colors:
#     print("this color in colors list:", color)




#colors =  ["orange","blue","pink","red"]
#colors[2] = "brown"
#colors.insert(1,"black")
#range(start,stop,step)
#for i in range(1,100,5):
    #print(i)
    
# names = []
# for i in range(1,5):
#     print("the name,(",i,"):")
#     name = input("whats your name?\n")
#     names.append(name)
    
    
    
    
# print(names)





#break

#test = [12,8,7,5,36,2,1,3]


# colors = ["red","blue","orange","pink","yellow"]



# for x in colors:
#     print(x)
#     if len(x) >= 4:
#         break


# colors = ["red","blue","orange","pink","yellow"]        

# for i in colors:
#     if not len(i) == 4: #age not bezarim chizi ke mikhaym ro neshonm mide 
#         continue #daghighan abraks kar mikone ma goftim 4ta caractor bashe ama vaghti az in estefade mnikonim baraks neshon mide 
#     print(i)


# for i in colors:
#     if i == "orange": #inja ma nemikhaym orange ro bebinim bara hamion az continue estefade mikonim 
#         continue
#     print(i)
    

# x = [12,3,67,98,34,1,5]

# for i in x:
#     if i == 67 or i ==5: #ma na 67 ro darim dg va na 5 chon ma khastim inaro neshon nade ... age not bezarim faghat 67 va 5 ro neshon mide 
#         continue  #az not yebar mishe estefade kard dakheil sharrt
    
#     print(i)


# x = [12,3,67,98,34,1,5]

# for i in x:
#     if i % 2 == 0:
#         continue
#     print(i)
    
    
#list-for

# name = ["mina","mahshid","alireza","sima","sina"]

# x = [i.upper() for i in name if "d" in i] 
# print(x)


# test = [12,23,44,78,6,8]
# x = [i/2 for i in test if i %2 ==0] #ghesmate aval mitoni tammae mohasebat ro anjam bedi mesle * / + _ % va ghesmate domom sharthaaa 
# print(x)

