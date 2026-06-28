item1_name = "Notebook"
item1_price = "4.99"
item1_qty = "2"

item2_name = "Pen Pack"
item2_price = "7.50"
item2_qty = "1"

item3_name = "Backpack"
item3_price = "34.99"
item3_qty = "1"

tax_rate = "0.075"

item1_price_num = float(item1_price)
item2_price_num = float(item2_price)
item3_price_num = float(item3_price)

item1_qty_num = int(item1_qty)
item2_qty_num = int(item2_qty)
item3_qty_num = int(item3_qty)
tax_rate_num = float(tax_rate)

item1_total = item1_price_num * item1_qty_num
item2_total = item2_price_num * item2_qty_num
item3_total = item3_price_num * item3_qty_num

subtotal = item1_total + item2_total + item3_total
tax = subtotal * tax_rate_num
grand_total = subtotal + tax

print("=" * 35)
print("      STORE RECEIPT")
print("=" * 35)

print(f"{item1_name} x{item1_qty_num} ${item1_total:.2f}")
print(f"{item2_name} x{item2_qty_num} ${item2_total:.2f}")
print(f"{item3_name} x{item3_qty_num} ${item3_total:.2f}")

print("=" * 35)

print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax: ${tax:.2f}")
print("=" * 35)
print(f"Grand Total: ${grand_total:.2f}")



