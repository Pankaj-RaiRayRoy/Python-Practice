numbers = input("Enter five different numbers separated by space: ")
list_numbers = numbers.split()

for counter in range(len(list_numbers)):
    list_numbers[counter] = int(list_numbers[counter])

print("Your list is: ", list_numbers)
print("The largest number in the list is: ", max(list_numbers))


"""
this program asks the user to enter five different numbers....then returns the list in integer form.
It also prints out the largest member of the provided list using the inbuild max() function

"""
