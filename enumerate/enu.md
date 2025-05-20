The enumerate() function in Python adds a counter to an iterable and returns it as an enumerate object. This object yields pairs of the form (index, element), allowing for simultaneous access to both the index and value of each item in the iterable during iteration. 
Python

my_list = ['apple', 'banana', 'cherry']
for index, value in enumerate(my_list):
    print(f"Index: {index}, Value: {value}")


This will output:
Code

Index: 0, Value: apple
Index: 1, Value: banana
Index: 2, Value: cherry


The enumerate() function can also take an optional start argument, which allows you to begin the counter at a specific number, instead of the default 0.
Python

for index, value in enumerate(my_list, start=1):
    print(f"Index: {index}, Value: {value}")


This will output:
Code

Index: 1, Value: apple
Index: 2, Value: banana
Index: 3, Value: cherry