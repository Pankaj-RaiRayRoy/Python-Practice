numbers = input("Enter five numbers separated by spaces: ")
list_numbers = numbers.split()

for counter in range(len(list_numbers)):
    list_numbers[counter] = int(list_numbers[counter])

print("Your list is: ", list_numbers)

largest = list_numbers[0]

for counter in range(len(list_numbers)):
    if list_numbers[counter] > largest:
        largest = list_numbers[counter]

print("The largest element is : ", largest)

"""
this program manually checks for the largest element in the given list
"""
