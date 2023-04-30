#palindaroom
#mesal mum=mum 

def plaindarome(text):
    if text == text[::-1]:
        return True #mitonim jaye return az print use konim 
    else:
        return False
    
text = input("please enter your text:\n") 
plaindarome(text)
