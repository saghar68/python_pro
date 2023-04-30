name = ["mina","mahshid","alireza","sima","shima","ali","sina"]

# x = [i.replace("m","l",1) for i in name] # aval harf m ro tagghir bede ba l
# print(x)

#x = [i.title() for i in name if len(i) == 5] #mosavi ba 5
#x = [i.title() for i in name if len(i) < 5] #kochiktar az 5
x = [i for i in name if "ali" in i] #onaei ke ali hastan ro neshon bede 
print(x)
