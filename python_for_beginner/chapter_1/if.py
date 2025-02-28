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

# Python Calculator

operator = input("Enter an operator (+, -, *, /): ")

# Validate first number
while True:
    try:
        num1 = float(input("Enter the 1st number: "))
        break
    except ValueError:
        print("Please enter a valid number!")

# Validate second number
while True:
    try:
        num2 = float(input("Enter the 2nd number: "))
        if operator == "/" and num2 == 0:  # Prevent division by zero
            print("Division by zero is not allowed! Enter a different number.")
            continue
        break
    except ValueError:
        print("Please enter a valid number!")

# Perform Calculation
if operator == "+":
    print(f"The Addition of {num1} and {num2} is: {num1 + num2:.3f}")
elif operator == "-":
    print(f"The Subtraction of {num1} and {num2} is: {num1 - num2:.3f}")
elif operator == "*":
    print(f"The Multiplication of {num1} and {num2} is: {num1 * num2:.3f}")
elif operator == "/":
    print(f"The Division of {num1} and {num2} is: {num1 / num2:.3f}")
else:
    print(f"{operator} is not a valid operator!")


# Weight Converter

weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds? (K or L): ").upper()

if unit == "K":
    converted_weight = weight * 2.20462
    print(f"{weight} kilograms is equal to {converted_weight:.2f} pounds.")
elif unit == "L":
    converted_weight = weight / 2.20462
    print(f"{weight} pounds is equal to {converted_weight:.2f} kilograms.")
else:
    print("Invalid input! Please enter 'K' for Kilograms or 'L' for Pounds.")
