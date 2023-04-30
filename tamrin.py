#6037_9971_5422_0959
def card_number(number):
    x = "*" * 15 + number[-4:]
    return x

num = input("enter your Phone: ")
print(card_number(num))