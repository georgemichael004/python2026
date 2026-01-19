# Q: How do small helper functions combine into one result?
def calculate_subtotal(price, quantity):
    return price * quantity
def calculate_tax(subtotal, tax_rate=0.075):
    return subtotal * tax_rate
def calculate_total(subtotal, tax):
    return subtotal + tax

def process_sale(price, quantity):
    """Main function to process the entire sale."""
    subtotal = calculate_subtotal(price, quantity)
    tax = calculate_tax(subtotal)
    total = calculate_total(subtotal, tax)
    print(f"Subtotal: ${subtotal:.2f}, Tax: ${tax:.2f}, Total: ${total:.2f}")

process_sale(10.00, 3)
