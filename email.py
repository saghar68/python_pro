email = input("Please Enter You'r Email adress!:\n")
gmail = "saghi.abazari@gmail.com"
yahoo = "saghi.abazari@yahoo.com"

if email.isdigit() == False:
   if email == gmail:
       print("You'r welcome, You use a gmail account ")    
   if email == yahoo:
       print("You'r welcome, You use a yahoo account ")
   elif email != gmail and yahoo :
       print("You use diffrent email")
else:      
   print("You Entered Symbol's, Please Enter Your Email Address")  