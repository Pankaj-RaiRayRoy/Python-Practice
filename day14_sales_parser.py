total_revenue = 0
total_expense = 0

try:
    with open("day14_daily_sales.txt", "r") as file:
        for line in file:
            line = line.strip()
            new_line = line.split(" ")
            if new_line[0] == "Revenue:":
                total_revenue = total_revenue + int(new_line[1])
            if new_line[0] == "Expense:":
                total_expense = total_expense + int(new_line[1])

except FileNotFoundError:
    print("Please Enter the correct file name!!")

profit = total_revenue - total_expense



with open("financial_summary.txt", "w") as file:
    file.write("   --- FINANCIAL SUMMARY ---   \n")
    file.write(f"Total Revenue: {total_revenue}\n")
    file.write(f"Total Expense: {total_expense}\n")
    file.write(f"Net Profile: {profit}\n")

with open("financial_summary.txt", "r") as file:
    content = file.read()
    print(content)
