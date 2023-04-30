weakly = ["monday" ,"tuesday","wensday","thursday","friday","saturday", "sunday"] 

user = input("what day today?:\n")

if user.isdigit() == False:
   if user == weakly[0]:
       print('today is Monday and we are in the office')
   elif user == weakly[1]:
       print('today is tuesday we are not in the office please send a message thank you.')
   elif user == weakly[2]:
       print('today is wensday and we are busy , cant answer the phone .')
   elif user == weakly[3]:
       print('today is thursday and we are busy')
   elif user == weakly[4]:
       print('today is friday , the office close at 12 oclock')
   elif user == weakly[5]:
       print('today is saturday :) we are close just enjoing your day guys')
   elif user == weakly[6]:
       print('today is sunday , be ready tomarrow you need come back to the office ;)')
else:
    print("you enter symbol's, please enter a string ")
print("have a lovely day ")
    



