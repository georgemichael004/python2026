def calculate_discount(purchase_amount: float, is_member):
    if purchase_amount <= 0:
            return 0.0
    
    if purchase_amount > 200:
       purchase_amount *= (100-20)/100
    elif purchase_amount > 100:
        purchase_amount *= (100-15)/100
    elif purchase_amount > 50:
        purchase_amount *= (100-10)/100

    
    if is_member == True:
        purchase_amount *= (100-5)/100
    return round(purchase_amount, 2)

print(calculate_discount(250, True))

