try:
    with open("day14_raw_users.txt", "r") as source_file, open("day14_clean_users.txt", "w") as target_file:
        target_file.write("   ---CLEAN REGISTRATION LIST---   \n")
        for line in source_file:
            line = line.strip()
            new_line = line.split(",")
            user_name = new_line[0].strip()
            state_name = new_line[1].strip()
            if not state_name:
                continue
            else:
                clean_user_name = user_name.replace("_", " ").title()
                target_file.write(f"Name: {clean_user_name} | State: {state_name}\n")

except FileNotFoundError:
    print("Wrong File Name !!")

with open("day14_clean_users.txt", "r") as file:
    for line in file:
        print(line.strip())
