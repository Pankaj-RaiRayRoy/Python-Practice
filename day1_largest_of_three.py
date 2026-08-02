number1 = int(input("Enter the first distinct number : "))
number2 = int(input("Enter the second distinct number : "))
number3 = int(input("Enter the third distinct number : "))

if number1 > number2:
    if number1 > number3:
        print("First one is the largest of three!")
    else:
        print("Third one is the largest number!")
elif number2 > number3:
    print("The second number is the largest!")
else:
    print("The third one is the largest!")
