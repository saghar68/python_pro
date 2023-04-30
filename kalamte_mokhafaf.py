user_input = input("enter words:\n")
text = user_input.split()
a = " "
for i in text:
    a = a + i[0].upper()
    print(a)
    