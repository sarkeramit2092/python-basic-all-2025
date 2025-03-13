numbers = [1,-2,3,-4,5,6,-7,-8,9,10]

count = 0
for i in numbers:
  if i > 0:
    print(f"Each Positive Number: {i}")
    count += 1
print (f"Total positive number: {count}")
