✅ **Python List of Dictionaries Example:**
```python
data = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30}
]


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
