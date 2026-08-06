# Format: "Item Name": [Quantity In Stock, Price Per Unit]
warehouse_stock = {
    "laptop":[10, 1200],
    "mouse":[50, 25],
    "monitor":[20, 300],
    "keyboard": [0, 45]     # Out of stock item!
}

grand_total = 0
print("   ---WAREHOUSE VALUATION REPORT---   ")

for item_counter, item_price in warehouse_stock.items():
    total = item_price[0] * item_price[1]
    grand_total = grand_total + total
    if total == 0:
        print(item_counter, "- Total Value: ", total, "[CRITICAL: OUT OF STOCK]")
    else:
        print(item_counter, "- Total Value: ", total)

print("\nTotal Warehouse Value: ", grand_total)
