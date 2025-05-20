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


print(data[0]["id"])  # Access "id" from the first dictionary in the list

for person in data:
    print(person["id"])


'''
Yes — enumerate() is helpful when you want to loop through a list and also keep track of the index.
✅ When to Use enumerate()
Use enumerate() when:
You want to loop through all items in a list,
And you also need to know the index during the loop.
'''

for x,y in enumerate(data):
    print (x, y)
    print("-" * 30)
'''
✅ What’s Happening:
enumerate(data) returns a tuple of (index, value) for each item in the data list.

x gets the index.

y gets the actual dictionary (each person) in the list.
'''

for index,person_info in enumerate(data):
    #print (index, person_info)
    print(person_info["name"])
    print (person_info["address"]["city"])
    print("-" * 30)

for r in data:
    print(r)
    print("-" * 30)
    print(r["name"])
'''


'''
print("-" * 30)
print(data[0]["skills"][0])