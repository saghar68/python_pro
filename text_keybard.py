# keyboard_symbols = """}{_+=*()^£%$#&@!>:";/'"""
# text = input("please enter your text:\n")
# new = ""

# for x in text:
#     if x not in keyboard_symbols:
#         new = new+x

# print(new)



#horofi ke nemikhaym neshon bede ro ba in code  mishe anjam dad 

h = ("a", "o")
message = input("please send youre  youre message:\n")
msg = ""

for i in message:
    if i not in h:
        msg = msg +i
print(" my new message with correct word:  %s"%(msg))
    