price = float(input("Enter the price of the product: "))
quantity = int(input("Enter the quantity of the product: "))
total_price = price * quantity
vat_price = total_price * 0.05
final_price = total_price + vat_price
print(f"Total price of the product: {total_price:.2f}")
print(f"Tax (5%): {vat_price:.2f}")
print(f"Final price of the product: {final_price:.2f}")
