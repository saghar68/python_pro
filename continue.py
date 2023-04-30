lettername = 0

for letter in "sagharabazari":
    lettername += 1
    if letter == "a" or letter == "r":
        continue
    print("letter", lettername, "is", letter)
    