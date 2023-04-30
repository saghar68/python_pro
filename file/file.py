#mode r bara khondan filhast az aval mikhone
# mode w bara khondan va neveshtane 
#mode a bara ezafe kardane 



#file = open("text.txt",'r')
#x = file.read(30) #dakhele read bar asas caractor mikhone vaghti behesh add midim
#x = file.readline() #ye khat ye khat mikhone 
#print(file.readlines())#in yeki fasele mindaze va mikhone az \n use mikone 
#file.close()





'''
inam ye nemone halghe ke hamon kar ro anjam mide 
'''
#for i in file:
    #print(i)
    
    
    
#ijade file
#w bara inke dakheili ye file benevisim az w use mikonim az aval minevise

#name = input("enter name file:")
#x= open(f"{name}.txt",'w') #vaghti az in ravesh use mikonim ye file txt bevojod miad 
#xx = open(f"{name}.py","w") #ba inam file python dorost mishe



#neveshtan dar file text
# t = open("text.txt","w") #mode w miad matne ghabli dar text file ro pak mikone va matne jadid ro mizare jash
# t.write("hello saghar your welcome\n")
# t.write("how old are you?\n") #\n ro mizarim ke fasele bezare age nazarim hame ro michasbone be ham 
# t.write("""
        
#         hello
#         amin
#         hajipour
#         khobi?
        
#         """)


#neveshtan dar list text 

# x = open("text.txt",'w')
# x.writelines(["ali\n","reza\n","nims\n","mina\n"]) #bayad \n ro bezarim 


#ezafe kardan 
#a bara add kardan hastesh 


# x = open("text.txt",'a')
# x.write("\namir")
# x.close




#peyda kardan file dar ye poshe dg 
# x = open(r'/Users/sagharabazari/Saghar Projects/test.py/saghar.txt','r') #az test.py copy kardam addres ro gozashtam inja 
# print(x.read())



file = open("text.txt","w")
file.write("hello amin")