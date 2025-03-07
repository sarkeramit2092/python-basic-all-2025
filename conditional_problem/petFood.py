animal = "Cat"
age = 10

if animal == "Dog" and age < 2:
    print ("Puppy Food")

elif animal == "Cat" and age > 5:
    print ("Senior cat food.")

else:
    print (f"No Food for your {animal}.")
    print (f"{age} years old.")