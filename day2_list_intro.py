numbers = input("Enter five numbers separated by spaces: ")
numbers_list = numbers.split()

for counter in range (len(numbers_list)):
    numbers_list[counter] = int(numbers_list[counter])

print("Your list is: ", numbers_list)





"""
Comment: this program asks the user to enter firve different numbers separated by space.
#Then with the help of the split functions converts them into string value list members.
#then using the for loop function replaces each list member with its interger value. finally
it prints out the required list.

"""
