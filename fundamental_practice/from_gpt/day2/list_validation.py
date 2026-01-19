# Task: Check that a list has only integers and at least 5 items.
def list_validation(input_list):
    clean_list = []
    for item in input_list:
        if isinstance(item, int):
            clean_list.append(item)
        else:
            return "Provide only Integers"
        
    if len(input_list) >= 5:
        return "Yes, the list contains at least 5 elements"
    else:
        return "No, the list does not contain at least 5 elements"
    

testing_list = [1, 2, 3, 5, 6]
result = list_validation(testing_list)
print(result)
