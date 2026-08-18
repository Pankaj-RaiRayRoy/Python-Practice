office_assets = {
    "Risk" : 45,
    "Marketing" : 30,
    "Operations" : 60
}

print(office_assets["Operations"])
office_assets["Underwriting"] = 25
print(office_assets)
office_assets["Risk"] = 50

if "Finance" in office_assets:
    print("Finance Department exists.")
else:
    print("Finance Department does not exist.")

for department, count in office_assets.items():
    print(f"Department: {department} | Laptops : {count}")

try:
    print(office_assets["HR"])
except KeyError:
    print("Oops !! That department does not exist in our records.")
else:
    print("Information Access Complete!!")
finally:
    print("Have a nice day :) ")
