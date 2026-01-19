# Task: Loop through dictionary items to compute results.
products = {
    'Laptop': 990,
    'Smartphone': 600,
    'Tablet': 250,
    'Headphones': 70,
}

max_value = 0
best_product = " "

for key, value in products.items():
    if value > max_value:
        max_value = value
        best_product = key

print(f"The product wth the highest value is: {best_product} (${max_value})")
