student = {'name': 'john',
           'age': 20,
           'courses': ['math', 'compSci']
           }
# the update() method updates the dictionary with the elements from another dictionary object or from an iterable of key/value pairs. it takes either a dictionary or an iterable object of key/value pairs (as tuples or other iterables of length two) as an argument.
student.update({'name': 'jane',
                'age': 25,
                'phone': '555-5555'
                })

print(student)

# print(student['name'])
# student ['phone'] = '555-5555'
# print(student.get('age'))
# # print(student.get('phone', 'not found'))
# print(student.get('phone', 'not found'))