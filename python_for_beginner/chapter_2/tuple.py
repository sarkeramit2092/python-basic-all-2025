my_tuple = (1,"hello",3.5)

print("hello" in my_tuple)

print (my_tuple.index(3.5))
print (my_tuple.count(1))

numbers = [10,30,20]
new_tuple = tuple (numbers)

print (type(numbers))
print (type(new_tuple))

# Unpacking
person = ("Amit","32","Software Engineer")

name, age, job = person

print (job)
print (name)
print (age)

# slicing

num_tuple=(88,70,89,29,39,79)
print(num_tuple[1:4])
