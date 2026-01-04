import json

# 1. Convert JSON string to dictionary
json_str = "{'name': 'Alex', 'age': 22, 'city': 'Chennai'}".replace("'", '"')
dict1 = json.loads(json_str)
print("1.", dict1)

# 2. Convert dictionary to JSON string
dict2 = {'id': 101, 'product': 'Laptop', 'price': 55000}
json_str2 = json.dumps(dict2)
print("2.", json_str2)

# 3. Read JSON file data.json and print key-value pairs
# (Assuming data.json exists)
try:
    with open("data.json", "r") as f:
        data_file = json.load(f)
    print("3.", data_file)
except FileNotFoundError:
    print("3. data.json file not found")

# 4. Write dictionary to student.json
student = {'name': 'Mia', 'age': 24, 'grade': 'A'}
with open("student.json", "w") as f:
    json.dump(student, f, indent=4)
print("4. student.json created")

# 5. Print department from nested JSON
emp_json = {'employee': {'name': 'John', 'age': 30, 'department': 'HR'}}
print("5.", emp_json['employee']['department'])

# 6. Update dictionary age & convert to JSON
d6 = {'name': 'Raj', 'age': 45}
d6['age'] = 50
print("6.", json.dumps(d6))

# 7. Print second item from JSON list
list_json = ['red', 'green', 'blue']
print("7.", list_json[1])

# 8. Print all user names from JSON
users_json = {'users': [{'id':1,'name':'Alex'}, {'id':2,'name':'Mia'}]}
print("8.", [user['name'] for user in users_json['users']])

# 9. Add new key & convert to JSON
d9 = {'name': 'Sam', 'age': 28}
d9['country'] = 'India'
print("9.", json.dumps(d9))

# 10. Create items.json & print total cost
items = [
    {'item': 'Pen', 'price': 10},
    {'item': 'Book', 'price': 50},
    {'item': 'Bag', 'price': 700}
]
with open("items.json", "w") as f:
    json.dump(items, f, indent=4)

total_cost = sum(i['price'] for i in items)
print("10. Total Cost =", total_cost)
