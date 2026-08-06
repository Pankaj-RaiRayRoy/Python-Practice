# The transaction database: "Username": [List of transaction amounts]
accounts = {
    "user_101":[3500, 1600],    # Total spend: 5100 (Over 5000 limit)
    "user_102":[10,20,30,40,50],   # 5 Transactions (Over 4 limit)
    "user_103":[12,15,16],     # Safe user
    "user_104": []                     # Empty user (Edge case)
}

print("--- SYSTEM FRAUD AUDIT REPORT ---")

for user, transaction in accounts.items():
    if sum(transaction) > 5000 or len(transaction) > 4:
        print(user, " is [HIGH RISK]")
    else:
        print(user, "normal user!")
