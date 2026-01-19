# Task: Validate dictionary structure and required keys.
data_to_validate = {
    'item_a': 100,
    'item_b': 50,
    # 123: 'item_c', # This would fail validation
}

for key, values in data_to_validate:
    if not isinstance(key, str):
        print("Every key should be of type string")
    elif not isinstance(values, int):
        print("Every value should be of type integer")

    

