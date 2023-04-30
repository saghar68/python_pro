# guess = int(input("Player1: Please enter your number: "))
# count_try = 0
# x = False


# while count_try < 5 and x == False:
#     player2 = int(input("Player2: Please enter your guess: "))
#     if player2 == guess:
#         print("Player2: you are win!")
#         x = True
#     elif player2 > guess:
#         print("player2: your guess is greater than the number! Plaese try again..")
#         count_try += 1
#     elif player2 < guess:
#         print("player2: your guess is smaller than the  number! Plaese try again..")
#         count_try += 1
# if x == False: 
#     print("Player2: you are lost!")
          







guess = int(input("Player1 : please enter youre number:" )) 
count_number = 1
x = False

while count_number < 5  and x == False:  
     player2 = int(input("Player2: please enter your number:" )) 
     if player2 == guess:
         print("you win :)")
     elif player2 > guess:
         print("Player2: your number bigger than the number please try again !")
         count_number += 1
     elif player2 < guess:
         print("Player2: your number smaller than the number please try again!")
         count_number +=1
if x == False:
    print("you are lost sorry !")