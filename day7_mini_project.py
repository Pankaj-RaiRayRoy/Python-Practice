total_valid_revenue = 0
corrupted_records_count = 0

with open("security_alerts.txt", "w") as file:
    file.write("  ===HIGH RISK SECURITY ALERTS===\n\n")

with open("raw_transactions.txt", "r") as file:
    next(file)
    for line in file:
        column = line.strip().split(",")
        try:
            row_revenue = int(column[2]) * int(column[3])
            if row_revenue >= 1000 :
                print(f"Risk Detected -> Item: {column[0]} bought by {column[1]} | Revenue: ${row_revenue}")
            with open("security_alerts.txt", "a") as file:
                file.write(f"Risk Detected -> Item: {column[0]} bought by {column[1]} | Revenue: ${row_revenue}\n")
                total_valid_revenue += row_revenue

        except Exception as e:
            corrupted_records_count += 1        

print("Executive Summary: Total Clean Transactions Revenue Processed : $", total_valid_revenue)
print("Executive Summary: Total corrupted Error Rows Bypassed: ", corrupted_records_count) 
