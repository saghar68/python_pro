

while try_count<5 and x==False:
    guess=int(input("player2:please guess a number:"))
    if guess==answer:
        print('player2:you won!')
        x=True
    elif guess>answer:
        print('your guess is greater than the answer')
        try_count+=1
    else:
        print('your guess is smaller than the answer')
        try_count+=1
        
if x==False:
    print("plyer2:you lost")