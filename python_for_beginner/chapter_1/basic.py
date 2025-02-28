#variable

first_name = "Amit"
print (f"hello {first_name}")

age = 25
print (f"You are {age} years old")

price = 10.99
print (f"The price is ${price}")

is_active =True
if is_active:
  print ("You are Online!!")
else:
  print (f"You are Offline!!")


# Typecasting

name = "Amit Sarker"
age = 30
print (type(age))
gpa = 3.2
is_stident = False

age = str(age)
print (age)
print (type(age))

name = bool(name)
print (name)
print (type(name))

name2 = "A"
name2 = bool(name2)
print (name2)

name3 = ""
name3 = bool (name3)
print (name3)