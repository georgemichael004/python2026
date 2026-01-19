
def analyze_sales(sales):
    if sales == []:
        return None
    total_sales = 0
    no_sales = 0
    best_sale = sales[0]
    best_day = 1
    for i, val in  enumerate(sales):
        total_sales += val
        if val == 0:
            no_sales += 1
        if val > best_sale:
            best_sale = val
            best_day = i + 1

        

    average_sales = total_sales/len(sales)
    above_days = []
    for i, val in enumerate(sales):
        if val > average_sales:
            above_days.append(i+1)

    return {
        "total_sales": total_sales,
        "average_sales": average_sales,
        "best_day": best_day,
        "best_sale": best_sale,
        "no_sales": no_sales,
        "above_average_days": above_days
    }
