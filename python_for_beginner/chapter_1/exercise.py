# Exercise

item = input("What item would you like to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many would you like?: "))
total = price * quantity

print(f"You have bought {quantity} x {item}{'s' if quantity > 1 else ''}")
print(f"Your total is: ${total:.2f}")

# Exercise

# Getting user inputs
adjective1 = input("Enter an adjective (description): ")
noun1 = input("Enter a noun (person, place, thing): ")
adjective2 = input("Enter an adjective (description): ")
verb1 = input("Enter a verb ending with 'ing': ")
adjective3 = input("Enter an adjective (description): ")

# Generating the story
print("\nHere is your Madlibs story:")
print(f"Today I went to a {adjective1} zoo.")
print(f"In an exhibit, I saw a {noun1}.")
print(f"The {noun1} was {adjective2} and {verb1}.")
print(f"I was {adjective3}!")