#moshakhas kone shomare vase che shahrie 

telephon_numabr = input("Please enter you telephon number:\n")


if len(telephon_numabr) == 11 and telephon_numabr.isdigit():
    print("this number is true")
    if telephon_numabr[0:4] == '0611':
        print("you code number for ahwaz city, we call you back soon :)")
    elif telephon_numabr[0:3] == '021':
       print("you code number for tehran city, we call you back soon :)")   
    elif telephon_numabr[0:3] == '031':
         print("you code number for esfahan city, we call you back soon :)") 
    else:
        print("i cant guess where city you live !")        
elif len(telephon_numabr) > 11 and telephon_numabr.isdigit():
    print("this  number is not true and number is long!!!")         
elif len(telephon_numabr) < 11 and telephon_numabr.isdigit():
    print("this  number is not true and number is short!!!")   
elif not telephon_numabr.isdigit():
    print("error..... try again please!!!")        
                  
else:
    print("this number its false!") 