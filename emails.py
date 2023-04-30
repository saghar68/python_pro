#ye email daryaft kon 
#saghi.abazari@gmail.com



email = input("please enter your email:\n").strip()

# hala bia .com ro az email joda kon 

###carbar = email[:email.index("@")] #[0:7] 7-1=6
##domin = email[email.index("@")+1:]#
#print(f"username:{carbar}, domin name = {domin}")


carbar = email[:email.index("@")]
domin = email[email.index("@") + 1:]
print(f"username:{carbar}, domin name: {domin}")
