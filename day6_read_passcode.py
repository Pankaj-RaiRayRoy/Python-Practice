with open("secret_passcode.txt", "r") as test:
    content = test.read()
    print("The hidden passcode is : ", content)
