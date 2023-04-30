import re


txt = 'hello how are you sara? nice too meet you sara'
#x=re.findall('sara',txt)
#x=re.split("\s",txt,1)
x=re.sub('\s','9',txt,1)
print(x)