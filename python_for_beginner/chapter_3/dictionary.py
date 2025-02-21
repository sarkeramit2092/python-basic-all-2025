student = {
    "name":"Amit",
    "age" : 30,
    "grade" : "A"
}

# print (student)
# print (student["name"])
# print (student.get("age"))

# student["grade"]="A+"
# print(student)

# print(student.keys())
# print(student.values())
# print(student.items())
# print(student.update({"city":"Dublin"}))
# print(student.pop("age"))
# print(student.popitem())


for key,value in student.items():
  print(f'{key}:{value}')

print ("name" in student)
print ("city" not in student)

employees={
  "emp1" : {"name":"Amit","age":30},
  "emp2" : {"name" : "Mita", "age":40}
}

print(employees)
print(employees["emp1"]["name"])
print(employees["emp2"]["age"])