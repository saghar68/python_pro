#filter

#filter(fun,list/...)

#adadi ke kochiktar az 18 hast ro neshon bede
#ma ba filter ye chize khas ya grohe khasi ke mikhaym ro mitonim be dast biarym 
# x=[12,23,45,678,89,9]
# xx = filter(lambda a:a<18,x)
# print(list(xx))



#hala mikhaym bebinim ke ina bakhshpazir hastan bar 2 ya na 

# x=[12,23,45,678,89,9]
# xx = filter(lambda a:a%2==0,x)#age ja yeki az = ye ! bezarim adad fard ro neshomn mide 
# print(list(xx))



# #stringahr ro mikhaym filter konim

# test =['sara','amin','mahshid','ali','ahmad','jafar']
# #x = filter(lambda i:len(i)==4,test)
# xx = filter(lambda a:'l' in a,test) #esmhaei ke l daran ro neshon bede
# print(list(xx))






#filter_dic

test = [
    {'name': "saghar",'age':14,'email':"saghi.yahho"},
    {'name': "amin",'age':18,'email':'abas.gmail'},
    {'name': "nima",'age':20,'email':'ss.gamil'},
    {'name': "musa",'age':19,'email':"musa.yahoo"}
]


x = filter(lambda i:i['name']=='nima',test)
print(list(x))
