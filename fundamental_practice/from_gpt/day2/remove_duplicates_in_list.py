# Task: Remove duplicate items while preserving original order.
def remove_duplicates_in_list(input_list):
    results = []
    for item in input_list:
        if item not in results:
            results.append(item)
            
    return results


my_list = [1, 2, 2, 3, 4, 4, 5]
result = remove_duplicates_in_list(my_list)
print(result)
