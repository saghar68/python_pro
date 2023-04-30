grade = []
 
for i in range(1,7):
    number= float(input(f"enter your score("+ str (i) +") :\n"))
    grade.append(number)
    print(grade)

#sum()
sum_number=sum(grade) #مجموع
a=len(grade)
text=f"this is my number:{grade}\n and sum number:{sum_number}\nremainder:{sum_number}/{a}={sum_number/a}"
print(text)
    


#karnameeeee
# numbers =[]
# for i in range(1,11):
#     print("the number, (",i,"):")
#     num = float(input("please enter your number:\n"))
#     numbers.append(num)
    

# print( numbers)
# x = sum(numbers) #sum ye methode hastesh ke adad dakhel list ro jam mikone 
# print(x/len(numbers))

    
    
    