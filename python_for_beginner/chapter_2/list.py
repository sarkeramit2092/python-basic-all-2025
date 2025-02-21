thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
# print(len(thislist))
# print(thislist[1:4])


# # print(thislist.append("lemon"))

# thislist.append("lemon")
# print(thislist)

# my_new_list = thislist.copy()
# print (my_new_list)

thislist.sort()
print (thislist)

print(thislist.count("apple"))
thislist.pop(2)
print(thislist)
thislist.extend([1,2,3])
print(thislist)

thislist.insert(99,2)
print(thislist)