database_connection_open = True

try:
    transaction_id = int("95420")
except ValueError:
    print("Error: Invalid Transaction Code Formatiing Detected.")
else:
    print("Success: Transaction data verified! Updating live analyst metrics dashboard...")
finally:
    database_connection_open = False
    print("System clean-up: Safely disconecting from the remote database server.")
