#کاراکترهایی که با یک عدد شاخص زوج هستن   


# word = input("please enter a word\n")
# print("your orginal word is:",word)
# size = len(word)

# for i in range (0,size-1,2):
#     print('index[',i,']',word[i])



#inam ye ravesh dg 

word = input("enter your word plz:\n")
print("YOUR ORGINAL WORD IS: ",word)

x = list(word)
for i in x[0::2]:
    print(i)
    
