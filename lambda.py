# x = lambda a:a**2

# for i in range(1,10):
#     print(x(i))

#mesal
# test = lambda a,b,c:a+b*b*c+b**a-b
# print(test(23,44,56))


#mesal
# test = lambda first,last:f"my name is:{first.title()} {last.upper()}"
# x = input("enter your name?\n")
# y = input("enter your family:\n")
# print(test(x,y))



#mesal
#test = lambda x,func:x+func(x)
#print(test(2,lambda x:x*x)) #2ta lambda ba ham dige 

#lambda hamon function hastesh ama ye khati 



#mesal


# test = lambda x:(x%2 and 'odd' or 'even')
# print(test(4))


#mesal
#test = lambda *args:sum(args)
#print(test(4,6,8,9,23,34,67,88776,3344,2334)) #omadim az args dar lambda use kardaim 


#mesal



def func(n):
    return lambda a: a**n #mitonim dakhele tabe az lambda estefade konim 

test = func(8)
test2 = func(2)
print(test(9))
print(test2(2))