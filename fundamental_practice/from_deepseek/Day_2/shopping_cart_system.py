from datetime import datetime

def save_receipt(customer_name):
    date_str = datetime.now().strftime("%Y-%m-%d")

    lines = []
    lines.append(f"Customer: {customer_name}")
    lines.append(f"Date: {date_str}")
    lines.append("Items:")

    subtotal = 0
    for product_id, details in shopping_cart.items():
        name = product_invetory[product_id]["name"]
       

product_invetory = {
    "P001": {"name": "Laptop", "price": 569.99, "stock": 10, "category": "Electronics"},
    "P002": {"name": "Smartphone", "price": 769.99, "stock": 20, "category": "Electronics"},    
}

shopping_cart = {
    "P001": {"quantity": 2}    
}

customer_details = {
    "name": "John",
    "member_status": True,
    "zip_code": 12345
}

def add_to_cart(product_id, quantity):
    if product_invetory[product_id]["stock"] < quantity:
        return False
    if product_id in shopping_cart:
        shopping_cart[product_id]["quantity"] += quantity
        return True
    shopping_cart[product_id] = {"quantity": quantity}
    return True
    
 
    


def remove_from_cart(product_id, quantity):
    if product_id not in shopping_cart:
        return False
    if quantity > shopping_cart[product_id]["quantity"]:
        return False
    shopping_cart[product_id]["quantity"] -= quantity    
        
    if shopping_cart[product_id]["quantity"] == 0:
        del shopping_cart[product_id]        
    return True
    
    


def view_cart():
    if not shopping_cart:
        return "Cart is empty"
    output = ""
    for product_id, details in shopping_cart.items():
        price = product_invetory[product_id]["price"]
        qty = details["quantity"]
        subtotal = price * qty
        output += f"{product_invetory[product_id]['name']} - {qty} @ {price} = {subtotal}\n"
    return output.strip()



def checkout(zip_code):
    total = 0.0

    for product_id, details in shopping_cart.items():
        qty = details["quantity"]
        price = product_invetory[product_id]["price"]
        total += qty * price

    if str(zip_code).startswith("9"):
        total *= 1.08
    else:
        total *= 1.06

    return total

def save_receipt(customer_name):
    date_str = datetime.now().strftime("%Y-%m-%d")

    lines = []
    lines.append(f"Customer: {customer_name}")
    lines.append(f"Date: {date_str}")
    lines.append("Items:")

    subtotal = 0.0
    for product_id, details in shopping_cart.items():
        name = product_invetory[product_id]["name"]
        price = product_invetory[product_id]["price"]
        qty = details["quantity"]
        item_total = price * qty
        subtotal += item_total
        lines.append(f"{name} - {qty} @ {price} = {item_total}")

    # discount (member)
    discount = 0.0
    if customer_details["member_status"]:
        if subtotal > 200:
            discount = subtotal * 0.20
        elif subtotal > 100:
            discount = subtotal * 0.15
        elif subtotal > 50:
            discount = subtotal * 0.10

    after_discount = subtotal - discount

    # tax based on zip
    if str(customer_details["zip_code"]).startswith("9"):
        tax = after_discount * 0.08
    else:
        tax = after_discount * 0.06

    total = after_discount + tax

    # loyalty points
    points = 0
    if customer_details["member_status"]:
        points = int(total // 10)

    lines.append(f"Subtotal: {subtotal}")
    lines.append(f"Discount: {discount}")
    lines.append(f"Tax: {tax}")
    lines.append(f"Total: {total}")
    lines.append(f"Loyalty Points: {points}")

    return "\n".join(lines)

       
    