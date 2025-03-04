#Min and Max Numbers

import math

random_numbers = [10,20,22,12,1,24,30]

def max_number():
  print ("Max Number: ",(max(random_numbers)))

def min_number():
  print ("Min Number: ",min(random_numbers))


max_number()
min_number()



#Replace Words in a String

my_string = "This is a string"

def replace_word():
  old_entry = input("Enter a word to replace: ")
  new_entry = input("Enter new word: ")

  if (old_entry not in my_string):
    print(f"{old_entry} not in string!")

  else:
    output = my_string.replace(old_entry,new_entry)
    print (f"Finally the string is: {output}")
  
replace_word()