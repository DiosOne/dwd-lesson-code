# --- USE: Dictionary Example ---
print("--- DICTIONARY: USE PHASE ---")
# Product inventory: item_name -> quantity
inventory = {
    "laptop_stand": 20,
    "usb_c_hub": 35,
    "wireless_mouse": 50,
    'webcam': 25
}
    
print(f"Initial inventory: {inventory}")

product_prices = {
    'laptop_stand' : 25,
    'usb_c_hub': 30,
    'ergonomic_keyboard': 75,
    'webcam': 200
}
print(f"{list(product_prices.keys())[0].replace('_', ' ').title()} Price is: ${product_prices['laptop_stand']}")

price_check= 'webcam'
in_stock= product_prices.get('webcam', 'Unavailable')
if price_check in product_prices:
    # print(f'Price is: ${product_prices['webcam']}')
    print(f"{list(product_prices.keys())[3].replace('_', ' ').capitalize()} Price is: ${product_prices['webcam']}")
else:
    print(f"Price of {price_check} is: {in_stock}")
    
# iii.Stock Alert



# # Accessing an item's quantity
# item_to_check = "usb_c_hub"
# if item_to_check in inventory: # Good practice to check existence
#     print(f"Quantity of {item_to_check}: {inventory[item_to_check]}")
# else:
#     print(f"{item_to_check} not found in inventory.")

# # Using .get() to safely access (avoids KeyError)
item_to_check_safe = "monitor_arm"
quantity_safe = inventory.get(item_to_check_safe, 0) # Default to 0 if not found
print(f"Quantity of {item_to_check_safe}: {quantity_safe}")

# # Adding a new item
# inventory["ergonomic_keyboard"] = 15
# print(f"Inventory after adding keyboard: {inventory}")

# Updating an existing item's quantity (e.g., a new shipment arrived)
inventory["laptop_stand"] += 10
inventory["usb_c_hub"] -= 3
print(f"Inventory after restocking laptop stands: {inventory}")

# Removing an item (e.g., discontinued)
# if "wireless_mouse" in inventory:
#     del inventory["wireless_mouse"]
#     print(f"Inventory after removing wireless mouse: {inventory}")

# Getting all keys, values, or items
print(f"All product names (keys): {list(inventory.keys())}")
print(f"All quantities (values): {list(inventory.values())}")
print(f"All inventory entries (items): {list(inventory.items())}")
print("-" * 30 + "\n")