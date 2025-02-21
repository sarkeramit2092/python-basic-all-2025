# Tuples in Python

## What is a Tuple?
A **tuple** is an ordered, immutable collection of elements in Python. Tuples are represented as comma-separated values inside parentheses.

### **Tuple Creation**
Tuples can contain elements of different data types.


# Creating a tuple
my_tuple = (1, "Hello", 3.5)
print(my_tuple)  # Output: (1, 'Hello', 3.5)

# Tuple Indexing
Tuples support zero-based indexing. The first element starts at index 0, and the last element is at length - 1.

# Accessing elements
print(my_tuple[0])  # Output: 1
print(my_tuple[1])  # Output: Hello

# Tuple Properties
Ordered: Elements have a defined order.
Immutable: Cannot be modified after creation.
Indexed: Supports indexing and slicing.
Efficient: Uses less memory compared to lists.

# Tuple Methods
1. count()
Returns the number of times a value appears in a tuple.

my_tuple = (1, 2, 2, 3, 2, 4)
print(my_tuple.count(2))  # Output: 3

2. index()
Finds the first occurrence of a specified value.

print(my_tuple.index(3))  # Output: 3

# Tuple Packing & Unpacking
You can pack multiple values into a tuple and unpack them into variables.

# Packing
person = ("Alice", 25, "Engineer")

# Unpacking
name, age, profession = person
print(name)  # Output: Alice

# Tuple Slicing
You can extract parts of a tuple using slicing.

numbers = (10, 20, 30, 40, 50)
print(numbers[1:4])  # Output: (20, 30, 40)

# Nested Tuples
Tuples can be nested inside each other.

nested_tuple = (1, (2, 3), (4, (5, 6)))
print(nested_tuple[2][1][0])  # Output: 5

# Tuple Conversion
Convert a list into a tuple using tuple().

my_list = [1, 2, 3]
my_tuple = tuple(my_list)
print(my_tuple)  # Output: (1, 2, 3)

# Checking Membership
Use in or not in to check for elements.

my_tuple = (10, 20, 30)
print(20 in my_tuple)  # Output: True

# Tuple vs List

Feature	                               Tuple	           List
Mutable?	                            ❌ No	         ✅ Yes
Faster?	                                ✅ Yes	         ❌ No
Uses Less Memory?	                    ✅ Yes	         ❌ No
Supports Methods Like Append()?	        ❌ No	         ✅ Yes

# Summary
Tuples are ordered, immutable, and efficient.
Useful when data should not change.
Supports indexing, slicing, and iteration.
Can store heterogeneous elements.