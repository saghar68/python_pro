#BMI mashin hesab salamat

weight = float(input("Please enter your weight in kg:\n")) 
height = float(input("Please enter your height in centimters:\n"))

height = height / 100
BMI = weight /(height * height)

if BMI > 0:
    if BMI <= 16:
        print("you are very underweight :( ")
    elif BMI <= 18.5:
        print("you are underweight :(")
    elif BMI <= 25:
        print("you are healty :) ")
    elif BMI <= 30:
        print("you are overweight :( ")
    else:
        print("you are overweight :( ")
else:
    print("somthing is wrong")