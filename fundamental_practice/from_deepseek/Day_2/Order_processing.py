invetory = {
    "P001": {"price": 2.50, "stock": 10},
    "P002": {"price": 4.00, "stock": 5}
}

def validate_order(order_id, order_items, shipping_zip):
    errors = []
    total = 0.0
    if not (order_id.startswith("ORD")and len(order_id) == 7 and order_id[3:].isdigit()):
        errors.append("Invalid order ID")
    if not (len(shipping_zip) == 5 and shipping_zip.isdigit()):
        errors.append("Invalid shipping zip code")

    for product_id, quantity in order_items:
        if product_id not in invetory:
            errors.append(f"Product {product_id} not found")
            continue
        if quantity <= 0:
            errors.append(f"Invalid quantity for product {product_id}")
            continue
        if quantity > invetory[product_id]["stock"]:
            errors.append(f"Insufficient stock for product {product_id}")
            continue
        price = invetory[product_id]["price"]
        total += price * quantity
        if total < 5:
            errors.append("Minimum order is $5.00")
        is_valid = len(errors) == 0
    return is_valid, errors, total



    