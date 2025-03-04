#string

str ="this is a string"

print(str)
print(type(str))

print(str.upper())
print(str.lower())
print(str.capitalize(str))
print(str.find("is"))

text = "Hello, world!"
index = text.index("world")
print(index)  # Output: 7

fname = "billy"
lname = "bunt"

x = fname.replace("b","W")
y = lname.replace("b", "C")
print (x,y)


#If & Else Conditionals

age = int(input("Enter your age: "))

if age > 18:
    print("You can drink in the US")
else:
    print("You can't drink!!")


#User Input

print("Enter your name: ")
name = input(">> ")

print ("Hello" + name)

# Flow Control Functions

import time

def function1():
    print("This ......\n")
    function2()

def function2():
    print("Is....\n")
    function3()

def function3():
    print("Flow...\n")
    fuction4()

def function4():
    print("Control for ever......\n")
    wait()

def wait():
    print("Waiting.......\n")
    time.sleep (3)
    function1()




#For Loop

letters = "abcd"

# for letter in letters:
#   print (f"This letter is {letter}")
#   print (f"This letter is {letters}")


for x in letters:
  print(x)
  if x == "c":
    print(f"We have reached {x}!!")
    break


# List Search

def search_word():
    list1 = ["dave", "bill","sid","joe"]

    while True:
        word = input("Enter a word to search: ")
        if word in list1:
          print(f"{word} found in the list!!")
          break
        else:
          print (f"{word} is not in the list!!")
search_word ()
