# Day 7: Business Analyst KPI Metric Aggregator

# Initialize dual-state tracking counters outside the processing loop
successful_depts = 0
other_depts = 0

# Stream the file row-by-row to evaluate operational achievements
with open("department_eval.txt", "r") as file:
    for line in file:
        # Check for multiple target string keywords inside the data row
        if "Met" in line or "Acquired" in line or "Successfully" in line:
            successful_depts += 1
        else:
            other_depts += 1

# Output the final calculated strategic summaries after the data connection closes
print("Departments meeting targets:", successful_depts)
print("Departments requiring review:", other_depts)
