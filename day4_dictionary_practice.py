products = {
    "laptop":1200,
    "mouse":25,
    "monitor":300
}

item_to_check = input("Enter the item you want to know the price of: ")

#print("The price of the item is :", products[item_to_check])

if item_to_check in products:
    print("The price of the item is :", products[item_to_check])
else:
    print("Wrong input !!")
