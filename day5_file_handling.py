with open("sales_data.txt", "r") as file:
    for line in file:
        print("Data Row Found", line.strip())
