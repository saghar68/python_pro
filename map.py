#map az map baraye list tuple dic set estefade mikonim chon bishtar az ye chiz vojod dare 
# def fun(x):
#     return x*2

# x=[12,34,5,6]



# test = map(fun,x)
# print(list(test))






#baham zarb shodan 
# def test(a,b):
#     return a*b


# x = [45,3,4,5,56]
# y = [34,55,2,6,77]


# z = map(test,x,y)
# print(list(z))





#esmaye do ta list ro gozashtim to ye listt 2ta yeki shodan 

# def test(x,y):
#     return x+y

# x = ("ali","mina","nima","sina")
# y = ("anelly","arti","ayaan","amin")

# a = list(map(test,x,y))
# print(a)





#teded horof ro dar miarim be len
# x = ("ali","mina","nima","sina")
# #y = list(map(list,x))
# z = list(map(len,x))
# print(z)



#adad ro tabdil mikonim be reshte dar darone list

# a = (12,3,5,7,8,9,4)
# x = map(str,a)
# print(list(x))



#x = ("ali","nima","asad","musa")

#b = map(str.upper,x) #str vaghti use konim mitonim be method hash dastresi dashte bashim mesle upper
#f = map(lambda s:s.upper(),x) # in hamon raveshe balas vali az lambda use kardim
#print(list(f)) 



#faza khaliii ro mikhaym bartaraf konim ba map, ba strip dar map faghat tonestim ja khali ro dorost konim ke onam strip khali bedone parantez (), ama . ro natonestim raf koim error dad banabarin az lambad use konim 

# x = ("..ali..","..nima..","..asad..","..musa..")
# ##xx = map(str.strip('.'),x)
# xx = map(lambda a:a.strip('..'),x)
# print(list(xx))



#ye mesale dg , zarb mikone 

# x = [12,3,4,2]
# b = map(lambda a:a*2,x)
# print(list(b))


#ye mesale dg pow()


# x = [12,3,4,2,8]
# y = [17,37,49,20]

# b = map(pow,x,y) #pow ye tabe hastesh ke be tavan miresone
# print(list(b))


#ye mesale dg flaot ke ashari mikone 
# x = [12,3,4,2,8]
# y = map(float,x)
# print(list(y))




#ye meslae dg bara int ke adad ro az ashari be normal tabdil mikone

# x = [12.4,3.5,4.9,2.9,8.0]
# y = map(int,x)
# print(list(y))


#ye meslae dg  har adad ro be tavan 2beresone ,ma 2bar be a goftim 2 ta kar ro anjam bede yebar be tavan2 berese yebar be tavan3 berese va omad ina ro gozashte to ye tuple 

# def square(a):
#     return a**2,a**3
    
        
# numbers = [12,2,34,5,66]
# s =map(square,numbers)
# print(list(s))





 # in hamon mesale balas yelam fargh karde 
 
# def square(a):
#     return a**2,a**3
    
        
# numbers = [1,2,3,4,5]
# x = [square(i) for i in numbers] #inja az list for use kardim , tabe square ro gozashtim to listfor
# print(x)



#ye mesale dg 

x = ["maral","sara","arti"]
#xx = map(lambda i:i.replace('a','b'),x) #replace estefade kardim
#xx = map(lambda s:len(s)==5,x) #map sharti benevisim ba true flase neshon mide
xx = map(lambda a:'a' in a,x) #inam ye nemone shart dg ke ba true false neshon mide 
print(list(xx))




