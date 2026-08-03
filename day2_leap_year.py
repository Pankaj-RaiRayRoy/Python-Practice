year = int(input("Enter a year that you want to test for being a leap year: "))

if year % 400 == 0:
    print("its a leap year !")
elif year % 100 == 0:
    print("Its not a leap year!")
elif year % 4 ==0:
    print("its a leap year!")
else:
    print("its not a leap year!")
