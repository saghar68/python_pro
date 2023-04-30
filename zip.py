#zip()
#bara zip kheili moheme ke tedad ba ham barabar bashe 
#dar zip mitoni ham list dashte bashi ham tuple ham set


# name = ["ali","sara","alireza"]#list
# family = ("abazari","hajipour","doostani")#tuple
# age = {14,12,17}#set


# x = zip(name,family,age)
# print(list(x))



#name = ["amir","sara","alireza","mina"]
#num = [22,12,20,16] 
#x = ["a","b","c","z"]

# for a,b,c in zip(name,num,x):
    
#     print('name:',a)
#     print('number:',b)
#     print('letter:',c)


#x = range(1,89)
#print(list(x)) 
 
 
# num = [22,12,20,16] 
# x = list(zip(num,range(2)))
# print(x)


# x = zip(range(1,10),range(1,101)) #ghanone zip inke oni ke kamtare ro neshon mide banabar in 1 ta 10 ro neshon mide 
# print(list(x))





#y  = list(zip(name,num))

#x = {i.title():j for i,j in zip(name,num) if "m" in i and j%2==0 }

#x= {i:j for i,j in zip(name,num)}
#x= {i.upper():j*2 for i,j in zip(name,num)} #dar zip dobare ma mitonim ghesmate aval taggirat ro bezarim va ghesmate dovom ke hamo j hast karaye mesle * ** / - + ro anjam bedim 
#print(x)





test = [1,2,3],[4,5,6],[7,8,9]

for i in zip(*test):#vaghti setare bezari miad daronrizi mikone
    print(i , end="")#vaghti end ro mizarim hame ro dar kenar ham neshon mide 


