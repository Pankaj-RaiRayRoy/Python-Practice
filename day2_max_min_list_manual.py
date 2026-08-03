#starting with the user input and populating the list
numbers = input("Enter five numbers separated by spaces: ")
list_numbers = numbers.split()

#converting every element into integer:-
for counter in range(len(list_numbers)):
    list_numbers[counter] = int(list_numbers[counter])

#printing the integer output
print("Your list is : ", list_numbers)

#searching the largest:-
largest = list_numbers[0]
for counter in range(len(list_numbers)):
    if list_numbers[counter] > largest:
        largest = list_numbers[counter]

print("The largest element is : ", largest)

#searching for the smallest:-
smallest = list_numbers[0]
for counter in range(len(list_numbers)):
    if list_numbers[counter] < smallest:
        smallest = list_numbers[counter]

print("The smallest element is : ", smallest)
