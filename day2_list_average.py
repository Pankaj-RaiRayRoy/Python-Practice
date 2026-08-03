#taking the user input and populating the list.
numbers = input("Enter few numbers separated by spaces: ")
list_numbers = numbers.split()

#converting each member into an integer value.
for counter in range(len(list_numbers)):
    list_numbers[counter] = float(list_numbers[counter])

total = 0

for counter in range(len(list_numbers)):
    total = total + list_numbers[counter]

average = total / len(list_numbers)

print("The average of the list is: ", average)
