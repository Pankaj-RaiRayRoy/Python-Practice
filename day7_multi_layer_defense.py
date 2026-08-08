try:
    with open("system_config.txt", "r") as file:
        for line in file:
            print(line.strip())

except FileNotFoundError:
    print("⚠️ Error: That file does not exist on this drive.")

except PermissionError:
    print("🔒 Security Error: You do not have the required clearance to access this file.")
