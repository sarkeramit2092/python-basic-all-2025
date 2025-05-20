✅ **Python List of Dictionaries Example:**
```python
data = [
    {"name": "Alice", "age": 25},   # ← First dictionary (index 0)
    {"name": "Bob", "age": 30}      # ← Second dictionary (index 1)
]
# This is a list containing two dictionaries.


print (data[0]["name"])
print("-"*30)


'''
You're getting an error because data is a list, and you're trying to use .get("name"), which is a method for dictionaries, not lists.

print(data.get("name"))

'''

print(data[0].get("name"))  # Output: Alice
print("-"*30)


print(data[0].keys())  # Output: dict_keys(['name', 'age'])
print(data[1].values())  # Output: dict_values(['Bob', 30])


for key, value in data[0].items():
    print(key, value)
    print("-"*30)
# Output:
# name Alice
# age 25

for data in data:
  print (data["name"])
  print("-"*30)

```  

📌 Accessing Values using Key Names:

```python
print(data[0]["name"])  # Output: Alice
```
📌 Accessing Values using get() Method:

```python
print(data[1].get("age"))  # Output: 30
```
📌 Accessing Keys using keys() Method:

```python
print(data[0].keys())  # Output: dict_keys(['name', 'age'])
```
📌 Accessing Values using values() Method:

```python
print(data[1].values())  # Output: dict_values(['Bob', 30])
```
📌 Accessing Items using items() Method:

```python

for key, value in data[0].items():
    print(key, value)
# Output:
# name Alice
# age 25
```


✅ **Complex Python List of Dictionaries Example:**
```python
data = [
    {
        "id": 1,
        "name": "Alice",
        "age": 25,
        "skills": ["Python", "Docker"],
        "address": {
            "city": "New York",
            "zip": "10001"
        }
    },
    {
        "id": 2,
        "name": "Bob",
        "age": 30,
        "skills": ["Java", "AWS"],
        "address": {
            "city": "San Francisco",
            "zip": "94105"
        }
    }
]
