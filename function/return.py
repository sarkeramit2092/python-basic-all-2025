# return = statement used to end of a function
#          and send a result back to the caller.

def add(x, y):
    z = x+y
    return z   #after we finish the function a value is returned 

def multiply(x, y):
    z = x*y
    return z

print(add(1,2))  #this function becomes whatever is returned --> print(3)
print(multiply(250,2))   # --> print(500)


def create_name(first_name,last_name):
    first_name = first_name.capitalize()
    last_name = last_name.capitalize()
    return first_name+" "+last_name

full_name = create_name("amit", "sarker")
print(full_name)

#using the return statement we can return some data back to the place which we call a function.