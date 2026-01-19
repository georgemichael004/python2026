# Task: Filter dictionary entries based on a condition.
products = {
    'Laptop': 990,
    'Smartphone': 600,
    'Tablet': 250,
    'Headphones': 70,
}

filtered_products = {}

for key, value in products.items():
    if value > 50:
        filtered_products[key] = value

print("The filtered products are", filtered_products)
