# Day 7: Memory-Efficient Line-by-Line Reader

# Open the file stream and read line-by-line using a memory-safe loop
with open("department_eval.txt", "r") as file:
    for line in file:
        # Using .strip() shaves off trailing whitespace and hidden file newline characters (\n)
        print(line.strip())
