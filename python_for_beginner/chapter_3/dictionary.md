# Dictionary in Python

## What is a Dictionary?
A **dictionary** is an **unordered**, **mutable**, and **key-value** based collection in Python. It allows fast data lookup and is defined using curly braces `{}`.

### **Dictionary Creation**
Dictionaries store data in **key-value pairs**, where **keys must be unique and immutable**.

# Creating a dictionary
student = {
    "name": "Alice",
    "age": 25,
    "grade": "A"
}
print(student)  # Output: {'name': 'Alice', 'age': 25, 'grade': 'A'}

# Accessing Values
Values are accessed using keys.

print(student["name"])  # Output: Alice
print(student.get("age"))  # Output: 25

# Modifying a Dictionary
Dictionaries are mutable, so values can be updated.

student["grade"] = "A+"
print(student)  # Output: {'name': 'Alice', 'age': 25, 'grade': 'A+'}

# Dictionary Methods
1. keys()
Returns all the keys in the dictionary.

print(student.keys())  # Output: dict_keys(['name', 'age', 'grade'])

2. values()
Returns all the values in the dictionary.

print(student.values())  # Output: dict_values(['Alice', 25, 'A+'])

3. items()
Returns key-value pairs as tuples.

print(student.items())  
# Output: dict_items([('name', 'Alice'), ('age', 25), ('grade', 'A+')])

4. update()
Updates the dictionary with another dictionary or key-value pair.

student.update({"city": "New York"})
print(student)  
# Output: {'name': 'Alice', 'age': 25, 'grade': 'A+', 'city': 'New York'}

5. pop()
Removes a key-value pair and returns its value.

age = student.pop("age")
print(age)  # Output: 25
print(student)  # Output: {'name': 'Alice', 'grade': 'A+', 'city': 'New York'}

6. popitem()
Removes and returns the last inserted key-value pair.

last_item = student.popitem()
print(last_item)  # Output: ('city', 'New York')

7. clear()
Removes all elements from the dictionary.

student.clear()
print(student)  # Output: {}

# Dictionary Iteration
Dictionaries can be looped using for loops.

for key, value in student.items():
    print(f"{key}: {value}")

# Dictionary Nesting
A dictionary can contain another dictionary.

employees = {
    "emp1": {"name": "John", "age": 30},
    "emp2": {"name": "Emma", "age": 28}
}
print(employees["emp1"]["name"])  # Output: John

# Dictionary Comprehension
Similar to list comprehension, dictionaries can be created using one-liners.

squares = {x: x*x for x in range(1, 6)}
print(squares)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Checking Membership
Use in to check if a key exists.

print("name" in student)  # Output: True
print("city" not in student)  # Output: True

# Dictionary vs List

Feature	                         Dictionary	             List
Key-Value Pair?	                     ✅ Yes	           ❌ No
Ordered (Python 3.7+)?	             ✅ Yes	           ✅ Yes
Mutable?	                         ✅ Yes	           ✅ Yes
Allows Duplicate Keys?	             ❌ No	           ✅ Yes
Lookup Speed	                     🚀 Fast	        🐌 Slow (for large lists)

# Summary

Dictionaries store key-value pairs.
Mutable, unordered, and fast for lookups.
Supports various built-in methods like keys(), values(), pop(), update(), and items().
Useful when data needs to be mapped (e.g., storing user info, configurations, and database records).