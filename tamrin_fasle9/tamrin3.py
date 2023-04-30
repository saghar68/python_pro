#کاراکتور اول رو از یک رشته حذف کنید


def remove_string(word,n):
    x = word[n:]
    return x

string= input("enter your text:\n")
number = int(input("enter your number for remove:\n"))
print("orginal string",string)
print("string:",remove_string(string,number))