# List in Python

A List in Python represents a collection of comma-separated values of any data type enclosed in square brackets.

var_name = [element1, element2, ...]

These elements can be of different data types.
List Properties: Ordered, Indexed, Mutable, and Dynamic.

# Indexing
The position of every element in the list starts from 0 and goes up to length - 1.
my_list = [10, 20, 30, 40]
print(my_list[0])  # Output: 10
print(my_list[-1])  # Output: 40 (negative indexing)

# Empty List
Creating an empty list:
my_list = []
print(my_list)  # Output: []

# List Methods
1. index method
Returns the index of the first occurrence of a specified value.
my_list = [1, 2, 3, 4, 2]
print(my_list.index(2))  # Output: 1

2. append method
Adds an element to the end of the list.
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4]

3. extend method
Adds the elements of a given iterable to the end of the list.
my_list = [1, 2, 3]
my_list.extend([4, 5, 6])
print(my_list)  # Output: [1, 2, 3, 4, 5, 6]

4. insert method
Inserts an element at a specified position.
my_list = [1, 2, 3]
my_list.insert(1, 99)
print(my_list)  # Output: [1, 99, 2, 3]

5. pop method
Removes the element at the specified position and returns it.
my_list = [1, 2, 3]
removed_item = my_list.pop(1)
print(removed_item)  # Output: 2
print(my_list)  # Output: [1, 3]

6. remove method
Removes the first occurrence of the specified value.
my_list = [1, 2, 3, 2]
my_list.remove(2)
print(my_list)  # Output: [1, 3, 2]

7. clear method
Removes all the elements from the list.
my_list = [1, 2, 3]
my_list.clear()
print(my_list)  # Output: []

8. count method
Returns the count of occurrences of a specified value.
my_list = [1, 2, 2, 3, 2]
print(my_list.count(2))  # Output: 3

9. reverse method
Reverses the order of the list.
my_list = [1, 2, 3]
my_list.reverse()
print(my_list)  # Output: [3, 2, 1]

10. sort method
Sorts the list in ascending order (default). Use reverse=True for descending order.
my_list = [3, 1, 4, 2]
my_list.sort()
print(my_list)  # Output: [1, 2, 3, 4]
my_list.sort(reverse=True)
print(my_list)  # Output: [4, 3, 2, 1]

11. copy method
Creates a shallow copy of the list.
my_list = [1, 2, 3]
copy_list = my_list.copy()
print(copy_list)  # Output: [1, 2, 3]

# Modifications to `copy_list` won't affect `my_list`.
copy_list.append(4)
print(my_list)  # Output: [1, 2, 3]
print(copy_list)  # Output: [1, 2, 3, 4]

# Other Useful Operations

List Slicing
Extracting a portion of a list:
my_list = [0, 1, 2, 3, 4, 5]
print(my_list[1:4])  # Output: [1, 2, 3]

Length of List
Finding the number of elements in a list:
my_list = [1, 2, 3]
print(len(my_list))  # Output: 3