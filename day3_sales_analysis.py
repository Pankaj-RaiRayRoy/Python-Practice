month_list = [] #empty list for months
sales_list = [] #empty list for sales value

entry_month = "" 
sales_amount = 0

while entry_month != "exit":
    entry_month = input("Enter the month(exit to stop): ")
    if entry_month == "exit":
        break
    else:        
        month_list.append(entry_month)

while sales_amount != "exit":
    sales_amount = input("Enter the sales amount (exit to stop): ")
    if sales_amount == "exit":
        break
    else:
        new_sales_amount = int(sales_amount)
        sales_list.append(new_sales_amount)

highest_sales = sales_list[0]
lowest_sales = sales_list[0]
total = 0
average_sales = 0

#calculating highest sales
for counter in range(len(sales_list)):
    if sales_list[counter] > highest_sales:
        highest_sales = sales_list[counter]

#calculating lowest sales
for counter in range(len(sales_list)):
    if sales_list[counter] < lowest_sales:
        lowest_sales = sales_list[counter]

index_highest = 0 
for counter in range(len(sales_list)):
    if sales_list[counter] == highest_sales:
        index_highest = counter

index_lowest = 0
for counter in range(len(sales_list)):
    if sales_list[counter] == lowest_sales:
        index_lowest = counter

#calculating the average
for counter in range(len(sales_list)):
    total = total + sales_list[counter]

average_sales = total / len(sales_list)

print("The highest sales month is :", month_list[index_highest])
print("The lowest sales month is :", month_list[index_lowest])
print("The average sales is :", average_sales)


print("The analysis of the data provided suggests tha the highest sales was in the month of ", month_list[index_highest], end ='')
print("and the lowest sales was in the month of ", month_list[index_lowest],".")
print("The average sales during the givne period was ", average_sales)
