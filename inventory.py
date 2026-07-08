inventory = {
    "laptop": {"price": 999.99, "quantity": 15},
    "mouse": {"price": 29.99, "quantity": 50},
    "hardrive": {"price": 99.99, "quantity": 30},
    "webcam": {"price": 49.99, "quantity": 75}, 
}

def display_inventory():
    print("=" * 40)
    print("            INVENTORY SHEET")
    print("=" * 40)
    print()

    if not inventory:
        print("No inventory remaining")
        return
    
    total_value = 0

    for product, info in inventory.items():
            product_value = (info["price"] * info["quantity"])
            print(f"    {product.capitalize()}")
            print(f"    Price: {info['price']}")
            print(f"    Quantity: {info['quantity']}")
            print()
            total_value = total_value + product_value
    print(f"Total Inventory Value: ${total_value:.2f}")    
    print("=" * 40)


display_inventory()

product = None

while product is None:
    search = input("Look up a product (enter product name): ").lower()
    product = inventory.get(search)

    if product: 
        print(f"Price: ${product['price']}")
        print(f"Quantity: {product['quantity']}")
    else: 
        print(f"No product found for '{search}'.")

update_product = input("Update Product: ").lower()

if update_product in inventory:
    new_quantity = int(input("Add Quantity: "))
    inventory[update_product]["quantity"] = new_quantity
    print("Product Inventory Updated. ")
    display_inventory()

else: 
     print("Product Not Found. ")

low_stock = set()

for product, info in inventory.items():
    if info["quantity"] < 10: 
        low_stock.add(product)

print("Low Stock Products: ")

if low_stock: 
    for product in low_stock:
        print(f"- {product.capitalize()}")
else:
     print("None")








        