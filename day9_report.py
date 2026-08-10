expense_list = []
new_corporate_expense = 500

with open("expenses.txt", "r") as file:
    for line in file:        
        expense_list.append(int(line.strip()))

expense_list.append(int(new_corporate_expense))

while 25 in expense_list:
    expense_list.remove(25)

total_cost = sum(expense_list)
print("The total cost is:", total_cost)
highest_cost = max(expense_list)
print("The highest transaction is :", highest_cost)
transaction_count = len(expense_list)
print("Total number of transactions is :", transaction_count)

expense_list.sort(reverse = True)

unique_element = expense_list[0]
counter = 1

print("The largest two transactions are : ", expense_list[:2])

with open("day9_report.txt", "w") as file:
    file.write(f"  ===Transactions Report===  \n")
    file.write(f"The Total Cost is : {total_cost}\n")
    file.write(f"The largest transactions is : {highest_cost}\n")
    file.write(f"The total number of transactions is : {transaction_count}\n")


    






