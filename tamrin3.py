#mom dad radar 
#esma ke baraks mishe dobare eine hame 

def plindrome(text):
    if text == text[::-1]:
      return True
    else:
      return False
  
print(plindrome('book'))
print(plindrome('radar'))