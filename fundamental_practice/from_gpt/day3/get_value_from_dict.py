# Task: Safely retrieve a value from a dictionary with a fallback.
my_dict =  {
    'name': 'Sam', 
    'age': 25, 
    'city': 'Nairobi'
    }
def get_value(my_dict, value):
    for key, val in my_dict.items():
        if val == value:
            return key
        else:
            return "Not found"
        
    
    
print(get_value(my_dict, 'Sam'))
