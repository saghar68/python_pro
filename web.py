#google.com
#site = input("please enter your website address:\n").strip()
#carbar = site[:site.index(".")]
#domin= site[site.index(".")+1:]
#print(f"name site:{carbar}, domin = {domin}")



#www.google.com 
site = input("please enter your website address:\n").strip()
carbar = site[site.index(".")+1:site.index(".",4)]
domin= site[site.index(".",4):]
print(f"name site:{carbar}, domin = {domin}")

