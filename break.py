#az carbar username mikhaym ke 6 ya 7 harf dashte bashe 

username = input("please enter username less than 6 charaters:\n").upper()
lettername = 1

for letter in username:
    print("letter", lettername, "is", letter)
    lettername += 1
    if lettername > 6:
        print("sorry ! your username is too long , please try again !")
        break
    