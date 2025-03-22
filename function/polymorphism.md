# Polymorphism in Python

## What is Polymorphism?
Polymorphism is an Object-Oriented Programming (OOP) concept that allows a function, method, or operator to behave differently based on the type of data it is working with.

## Types of Polymorphism
1. **Function Polymorphism** (Function Overloading & Method Overriding)
2. **Operator Polymorphism** (Operator Overloading)

## Function Polymorphism Examples

### Example 1: Function Handling Different Data Types
```python
# Function that works with different types of data
def multiply(a, b):
    return a * b

# Numeric multiplication
print(multiply(5, 3))       # Output: 15

# String repetition
print(multiply("Hello ", 3)) # Output: Hello Hello Hello
```

### Example 2: Method Overriding in Inheritance
```python
class Animal:
    def make_sound(self):
        return "Some sound"

class Dog(Animal):
    def make_sound(self):  # Overriding parent method
        return "Bark"

animal = Animal()
dog = Dog()
print(animal.make_sound())  # Output: Some sound
print(dog.make_sound())     # Output: Bark
```

### Example 3: Operator Overloading
```python
print(2 + 3)        # Output: 5 (Addition)
print("Hello " + "World")  # Output: "Hello World" (String concatenation)
print([1, 2] + [3, 4])  # Output: [1, 2, 3, 4] (List concatenation)
```

## Benefits of Polymorphism
✅ **Code Reusability** – The same function can handle multiple data types.  
✅ **Flexibility & Scalability** – Allows writing more generic and extensible code.  
✅ **Simplifies Code** – Reduces redundancy and improves readability.  

