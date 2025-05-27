file_path = 'products.txt'

# Read products.txt
with open(file_path, 'r') as f:
    lines = f.readlines()

# Process each line to extract product name, category, and price (convert price to float)
products = []
for line in lines:
    product_info = line.strip().split(':')
    product_name, category, price = product_info
    price = float(price)
    products.append([product_name, category, price])

# Create a list of dictionaries, where each dictionary represents a product
product_dicts = []
for product in products:
    product_dict = {
        'name': product[0],
        'category': product[1],
        'price': product[2]
    }
    product_dicts.append(product_dict)

# Write this list of product dictionaries to a new JSON file named products_export.json
import json
with open('products_export.json', 'w') as f:
    json.dump(product_dicts, f, indent=4)
    
print("Product Lists:")
for product_dict in product_dicts:
    print(product_dict)