word = input("Enter a string that you want to reverse: ")

for counter in range(0, len(word)):
    print(word[-counter-1], end="")
