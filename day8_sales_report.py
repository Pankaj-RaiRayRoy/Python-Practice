customer_repository = {}
total_revenue = 0
total_transactions = 0

def calculate_revenue(quantity, price_per_unit):
    return quantity * price_per_unit

with open("sales_data1.txt", "r") as file:
    next(file)  # Skip header row
    for line in file:
        row = line.strip().split(",")
        customer_name = row[1]
        
        # Calculate individual row metrics
        current_row_revenue = calculate_revenue(int(row[3]), int(row[4]))
        total_transactions += 1
        total_revenue += current_row_revenue
        
        # Accumulate customer metrics cleanly
        if customer_name in customer_repository:
            customer_repository[customer_name] += current_row_revenue
        else:
            customer_repository[customer_name] = current_row_revenue

# Initialize VIP tracking variables
vip_customer = ""
largest_spend = 0

# Extract keys and values using .items()
for customer, total_spent in customer_repository.items():
    if total_spent > largest_spend:
        largest_spend = total_spent
        vip_customer = customer

# Print clean summaries to your terminal
print("=== BUSINESS SALES REPORT ===")
print("Total Revenue:", total_revenue)
print("Total Transactions:", total_transactions)
print(f"VIP Customer: {vip_customer} (Spent: ${largest_spend})")

# Write out the file for documentation
with open("sales_summary.txt", "w") as out_file:
    out_file.write("=== BUSINESS SALES REPORT ===\n")
    out_file.write(f"Total Revenue: ${total_revenue}\n")
    out_file.write(f"Total Transactions: {total_transactions}\n")
    out_file.write(f"VIP Customer: {vip_customer} (Spent: ${largest_spend})\n")
