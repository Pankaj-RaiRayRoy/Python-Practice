try:
    with open("day14_system_logs.txt", "r") as read_file, open("critical_alerts.txt", "w") as write_file:

        write_file.write("   ---CRITICAL SECURITY ALERTS---   \n")

        for line in read_file:
            line = line.strip()
            new_line = line.split(" - ")
            if new_line[0] == "ERROR" or new_line[0] == "WARNING":
                write_file.write(f"ALERT: {new_line[1]}.\n")
            if new_line[0] == "INFO":
                continue
        
    with open("critical_alerts.txt", "r") as file:
        for line in file:
            print(line.strip())

except FileNotFoundError:
    print("Error: File untraceable !")

