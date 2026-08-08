# Day 7: Target-Specific Data Extraction Filter

# Open the log stream and isolate technical maintenance items using membership evaluation
with open("department_eval.txt", "r") as file:
    for line in file:
        # Check if the technical department flag is in the current stream row
        if "IT" in line:
            print(line.strip())
