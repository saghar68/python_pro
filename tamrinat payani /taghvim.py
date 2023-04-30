#sakhte taghvim 

import calendar


cal = 1
while cal != 0 :
    year = int(input("Please enter a year:\n"))
    months = int(input("Please enter a month:\n"))
    print(calendar.month(year,months))
    
