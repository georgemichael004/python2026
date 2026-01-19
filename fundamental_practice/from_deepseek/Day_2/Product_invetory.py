product_invetory = {
    "P001": {"name": "Laptop", "price": 569.99, "stock": 10, "category": "Electronics"},
    "P002": {"name": "Smartphone", "price": 769.99, "stock": 20, "category": "Electronics"},
    
}

def add_product(product_id, name, price, stock, category):
    if product_id in product_invetory:
        return False
    product_invetory[product_id] = {
        "name": name, "price": price, "stock": stock, "category": category
    }
    return True


def update_stock(product_id, new_stock):
    if new_stock < 0:
        return False
    if product_id in product_invetory:
        product_invetory[product_id]["stock"] = new_stock
        return True
    else:
        return False
    
def get_product_by_category(category):
    matches = []
    for product_id, details in product_invetory.items():
        if details["category"] == category:
            matches.append(product_id)
    return matches

def get_low_stock_products():
    low_stock = []
    for product_id, details in product_invetory.items():
        if details["stock"] < 10:
            low_stock.append(details)
    return low_stock


def calculate_total_invetory_value():
    total = 0
    for product_id, details in product_invetory.items():
        total += details["price"] * details["stock"]
    return total






