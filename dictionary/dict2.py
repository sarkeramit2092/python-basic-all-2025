data = {"id":101,
        "name":"Amit",
        "position":"CEO"}

for d in data:
  print(d, data[d])  


if "name" in data:
  print(f"Name of the CEO's is {data['name']}")


data3 = {
  "subject1":{"id":101,"name":"bangla"},
  "subject2":{"id":102,"name":"math"},
  "subject3":{"id":103,"name":"english"}
}

print(data3["subject1"])
print(data3["subject2"]["name"])



square_number = {x:x**2 for x in range(11)}

print (square_number)
square_number.clear()
print(square_number)
