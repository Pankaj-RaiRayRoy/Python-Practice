user_profile = {
    "Day" : 14,
    "Role" : "Business Analyst",
    "Language" : "Python",
    "Topic" : "File Handling"
}

try:
    with open("day14_report.txt", "w") as file:
        for key, value in user_profile.items():
            file.write(f"{key}: {value}\n")

except:
    print("Something is wrong my friend...review you code!!")

with open("day14_report.txt", "r") as file:
    for line in file:
        print(line)
