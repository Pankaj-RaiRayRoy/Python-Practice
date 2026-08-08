# Day 7: Revision Challenge - Multi-Mode File Handling

# 1. Read & Display the initial department evaluations
with open("department_eval.txt", "r") as file:
    content = file.read()
    print("--- Initial Department Evaluations ---\n")
    print(content)

# 2. Flag high-priority infrastructure note to a brand new file
with open("urgent_notice.txt", "w") as file:
    file.write("--- URGENT ATTENTION REQUIRED --- \n")
    file.write("Operations department requires immediate infrastructure funding !!")

# 3. Log an evaluation sign-off to the end of the file
with open("department_eval.txt", "a") as file:
    file.write("\n")
    file.write("EVALUATION CYCLE LOGGED: All department summaries archived.")

# 4. Final Verification: Read and print the updated log history
with open("department_eval.txt", "r") as file:
    content = file.read()
    print(content)
