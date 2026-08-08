# Day 7: Numerical Range Filtering and Data Analysis

# Open the flat database log matrix stream in read-only mode
with open("sales_manifest.txt", "r") as file:
    # Skip the operational metadata column headings row
    next(file)
    
    # Evaluate each transaction data row vector line-by-line
    for line in file:
        # Tokenize columns utilizing the comma delimiter character
        column = line.strip().split(",")
        
        # Calculate row-level macro financial metrics
        revenue = int(column[2]) * int(column[3])
        
        # Apply numerical filter constraint matrix (KPI Threshold >= $750)
        if revenue >= 750:
            # Render clean executive outputs using native string templates (f-strings)
            print(f"High revenue cohort -> Item {column[1]} | Total Revenue: ${revenue}")
