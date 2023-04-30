#بررسی کنید ایا اولین و آخرین شماره در یک لیست یکسان است ؟

#test
# def first_last(numberlist):
#     print("list",numberlist)
#     first = numberlist[0]
#     last = numberlist[-1]
#     if first == last:
#         return True
#     else:
#         return False
# num = [10,2,4,6,7,10]
# print(first_last(num))

# num = [2,4,5,6,7,8]
# print(first_last(num))








#test2 ino khodam code zadam ghati pati :)

# name = []
# for i in range(1,4):
#     name.append(int(input("Please enter your number:\n")))
# print(name) 
# def first_last(name):
#     first = name[0]
#     last = name[-1]
#     if first == last:
#         return True
#     else:
#         return False
# print(first_last(name))

     

num = []
for i in range(1,4):
    num.append(int(input("please enter your number:\n")))

print(num)

def first_last(num):
    first = num[0]
    last = num[-1]
    if first == last :
        return True
    else:
        return False

print(first_last(num))