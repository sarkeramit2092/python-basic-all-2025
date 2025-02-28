# #if statement = Do some code only if some condition is True. Else do something else.

age = int(input("Enter your age: "))

if age < 0:
    print("You haven't been born yet!")
elif age >= 18 and age < 100:
    print("You are now signed up!")
elif age >= 100:
    print("You are too old to sign up")
else:
    print("You must be 18+ to sign up")
# Exercise

response = input("Would you like food? (Y/N): ")

if response == "Y":
   print("Have some food!")
else:
   print("No food for you!")

# python calculator

operator = input("Enter an operator (+ - * /): ")

# Validate first number
while True:
    try:
        num1 = float(input("Enter the 1st number: "))
        if num1 == 0:
            print("Enter a valid number!!")
            continue
        break
    except ValueError:
        print("Please enter a valid integer!")

# Validate second number
while True:
    try:
        num2 = float(input("Enter the 2nd number: "))
        break
    except ValueError:
        print("Please enter a valid integer!")

if operator == "+":
    print(f"The Addition of {num1} and {num2} is: {num1 + num2}")
elif operator == "-":
    print(f"The Subtraction of {num1} and {num2} is: {num1 - num2}")
elif operator == "*":
    print(f"The Multiplication of {num1} and {num2} is: {num1 * num2}")
else:
    print(f"The Division of {num1} and {num2} is: {num1/num2}")
    