# json_examples.py
# Examples of JSON parsing, nested JSON, looping, and file operations in Python

import json

# -----------------------------
# 1. Basic JSON Parsing
# -----------------------------
person_json = '{"name": "Alice", "age": 30, "city": "Paris"}'

# Parse JSON string → Python dict
person = json.loads(person_json)

print("Basic JSON Parsing:")
print("Name:", person["name"])  # Alice
print("Age:", person["age"])    # 30
print("-" * 40)

# -----------------------------
# 2. Nested JSON
# -----------------------------
nested_json = '''
{
    "employee": {
        "name": "Bob",
        "age": 25,
        "skills": ["Python", "SQL", "Power BI"],
        "address": {
            "city": "London",
            "zipcode": "E1 6AN"
        }
    }
}
'''

data = json.loads(nested_json)

print("Nested JSON:")
print("Employee Name:", data["employee"]["name"])       # Bob
print("Second Skill:", data["employee"]["skills"][1])   # SQL
print("City:", data["employee"]["address"]["city"])     # London
print("-" * 40)

# -----------------------------
# 3. Looping through JSON data
# -----------------------------
employees_json = '''
[
    {"name": "Alice", "role": "Manager"},
    {"name": "Charlie", "role": "Developer"},
    {"name": "Eve", "role": "Analyst"}
]
'''

employees = json.loads(employees_json)

print("Looping through JSON:")
for emp in employees:
    print(emp["name"], "-", emp["role"])
print("-" * 40)

# -----------------------------
# 4. Writing JSON (dict → JSON string/file)
# -----------------------------
person_dict = {
    "name": "Diana",
    "age": 28,
    "city": "Berlin",
    "skills": ["Excel", "Power BI"]
}

# Convert dict to JSON string
person_json = json.dumps(person_dict, indent=4)
print("Writing JSON:")
print(person_json)

# Save to file
with open("person.json", "w") as f:
    json.dump(person_dict, f, indent=4)
print("Saved person.json file.")
print("-" * 40)

# -----------------------------
# 5. Loading JSON from a file
# -----------------------------
with open("person.json", "r") as f:
    person_from_file = json.load(f)

print("Loading JSON from file:")
print("Name:", person_from_file["name"])  # Diana