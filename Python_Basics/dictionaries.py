# Dictionaries in Python
# A dictionary is a collection of key-value pairs, where each key is unique.

student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

print(student)  # Output: {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
print(student['name'])  # Accessing value by key output: John
print(student['age'])   # Accessing value by key output: 25
print(student['courses'])  # Accessing value by key output: ['Math', 'CompSci']

# print(student['phone'])  # This will raise a KeyError since 'phone' key does not exist])
# print(student.get('phone'))  # Using get() method to avoid KeyError, output: None
# print(student.get('phone', 'Not Found'))  # Using get() with default value, output: Not Found

print(student.get('name'))  # Using get() method to access existing key, output: John

student = {1: 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
print(student[1])  # Accessing value by key output: John

student['phone'] = '555-5555'  # Adding a new key-value pair
student['name'] = 'Jane'  # Modifying an existing key's value

print(student)  # Output: {'name: 'Jane', 'age': 25, 'courses': ['Math', 'CompSci'], 'phone': '555-5555'}

student.update({'name': 'Mike', 'age': 26, 'phone': '123-4567'})  # Updating multiple key-value pairs

print(student)  # Output: {'name': 'Mike', 'age': 26, 'courses': ['Math', 'CompSci'], 'phone': '123-4567'}

# del student['age']  # Deleting a key-value pair using del

print(student)  # Output: {'name': 'Mike', 'courses': ['Math', 'CompSci'], 'phone': '123-4567'}

age = student.pop('age')
print(age)  # Output: 26

print(len(student))  # Getting the number of key-value pairs output: 4
print(student.keys())  # Getting all keys output: dict_keys(['name', 'courses', 'phone'])
print(student.values())  # Getting all values output: dict_values(['Mike', ['Math', 'CompSci'], '123-4567'])
print(student.items())  # Getting all key-value pairs output: dict_items([('name', 'Mike'), ('courses', ['Math', 'CompSci']), ('phone', '123-4567')])

for key, value in student.items():
    print(f"{key}: {value}")  # Iterating over key-value pairs and printing output: 