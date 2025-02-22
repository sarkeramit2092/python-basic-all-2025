# Set in Python

## What is a Set?
A **set** is an **unordered**, **mutable**, and **unindexed** collection of **unique elements** in Python. Sets are defined using curly braces `{}` or the `set()` function.

### **Set Creation**
Sets automatically remove duplicate values.

# Creating a set
my_set = {1, 2, 3, 4, 4, 5}
print(my_set)  # Output: {1, 2, 3, 4, 5}

# Creating an empty set (must use set(), not {})
empty_set = set()
print(type(empty_set))  # Output: <class 'set'>

# Set Properties
Unordered: No fixed order of elements.
Mutable: Can add or remove elements.
Unique Elements: No duplicates.
Unindexed: Cannot access elements using an index.

# Set Methods

1. add()
Adds an element to the set.

my_set.add(6)
print(my_set)  # Output: {1, 2, 3, 4, 5, 6}

2. update()
Adds multiple elements to the set.

my_set.update([7, 8, 9])
print(my_set)  # Output: {1, 2, 3, 4, 5, 6, 7, 8, 9}

3. remove()
Removes a specific element (raises an error if the element is not found).

my_set.remove(3)
print(my_set)  # Output: {1, 2, 4, 5, 6, 7, 8, 9}

4. discard()
Removes a specific element (does not raise an error if the element is missing).

my_set.discard(10)  # No error even if 10 is not in the set

5. pop()
Removes a random element from the set.

random_element = my_set.pop()
print(random_element)  # Output: Random element
print(my_set)  # Remaining elements

6. clear()
Removes all elements from the set.

my_set.clear()
print(my_set)  # Output: set()

# Set Operations

1. Union (| or union())
Returns a new set containing all unique elements from both sets.

set1 = {1, 2, 3}
set2 = {3, 4, 5}

union_set = set1 | set2
print(union_set)  # Output: {1, 2, 3, 4, 5}

2. Intersection (& or intersection())
Returns a new set containing common elements.

intersection_set = set1 & set2
print(intersection_set)  # Output: {3}

3. Difference (- or difference())
Returns elements present in the first set but not in the second.

diff_set = set1 - set2
print(diff_set)  # Output: {1, 2}

4. Symmetric Difference (^ or symmetric_difference())
Returns elements that are in either set, but not both.

sym_diff_set = set1 ^ set2
print(sym_diff_set)  # Output: {1, 2, 4, 5}

# Set Comparisons

1. issubset()
Checks if a set is a subset of another.

small_set = {1, 2}
print(small_set.issubset(set1))  # Output: True

2. issuperset()
Checks if a set is a superset of another.

print(set1.issuperset(small_set))  # Output: True

3. isdisjoint()
Checks if two sets have no common elements.

print(set1.isdisjoint({6, 7}))  # Output: True

# Checking Membership
Use in to check if an element exists.

print(2 in set1)  # Output: True
print(10 not in set1)  # Output: True

# Set vs List vs Tuple

Feature	               Set	      List	  Tuple
Mutable?	           ✅ Yes	✅ Yes	❌ No
Allows Duplicates?	   ❌ No	    ✅ Yes	✅ Yes
Indexed?	           ❌ No	    ✅ Yes	✅ Yes
Ordered?	           ❌ No	    ✅ Yes (Python 3.7+)	✅ Yes
Fast Lookups?	       ✅ Yes	❌ No	❌ No

# Summary
Sets store unique elements and are unordered.
Support mathematical operations like union, intersection, and difference.
Useful for fast lookups, removing duplicates, and set operations.