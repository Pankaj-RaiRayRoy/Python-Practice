number = int(input("Enter a number for factorial calcualtion: "))
total = 1

while number >= 1:

    if number == 1:  #line 6 through 8 takes care of the last part of the output
        print(number, " = ", end='')
        number -= 1
        break
    
    print(number, " X ", end = '')
    total = total * number
    number -= 1

print(total)
