number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

character = input("Choose the operation to perform ( +,-,*,/): ")

if character == '+':
    print("The addition of the two numbers is : ", number1 + number2)
elif character == '-':
    print("The subtraction of the two numbers is : ", number1 - number2)
elif character == '*':
    print("The multiplication of the two numbers is : ", number1 * number2)
elif character == '/':
    print("The division of the two numbers is : ", number1 / number2)
else:
    print("Wrong input !")
