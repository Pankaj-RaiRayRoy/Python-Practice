# Day 6: System Log Audit Management

# 1. Read and print current server logs
with open("server_logs.txt", "r") as file:
    content = file.read()
    print("--- Current Server Logs ---\n")
    print(content)

# 2. Filter critical alerts and overwrite into a new file
with open("critical_errors.txt", "w") as file:
    file.write("--- CRITICAL ERRORS --- \n")
    file.write("Nuclear bomb detection error !!")

# 3. Log a sign-off (Append to the end of the server logs)
with open("server_logs.txt", "a") as file:
    file.write("\n")
    file.write("AUDIT COMPLETED: All issues resolved or flagged.")

# 4. Final verification: Read and print the updated log history
with open("server_logs.txt", "r") as file:
    content = file.read()
    print(content)
