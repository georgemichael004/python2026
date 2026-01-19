# Task: Convert dictionary data into a list format.
products = {
    'Laptop': 990,
    'Smartphone': 600,
    'Tablet': 250,
    'Headphones': 70,
}

prices_list = list(products.values())
sorted_prices = sorted(prices_list)
print(sorted_prices)
