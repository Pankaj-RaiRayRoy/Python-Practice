# Day 7: Tabular Data Parsing and Revenue Calculation

# Open the flat file structure database stream in read mode
with open("sales_manifest.txt", "r") as file:
    # Safely bypass the metadata column headers line
    next(file)
    
    # Process the operational transaction records line-by-line
    for line in file:
        # Tokenize columns using comma delimiters
        column = line.strip().split(",")
        
        # Transform structural string variables into integers for financial math
        revenue = int(column[2]) * int(column[3])
        
        # Display clean calculated revenue logs to the executive dashboard
        print("Items : ", column[1], "| Total revenue $", revenue)
