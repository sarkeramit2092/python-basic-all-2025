# import os  #build in module
# #import flask  #pip install flask #external module

# from playsound import playsound

# print ("hello world")

# '''multiple lines'''

# # playsound()

greeting = "Good Morning, "
name = "Amit Sarker"
print(name[0:4:2])  #[:4:2]

c = greeting + name
print (f'Hello, {c}')

story = "In the heart of the village, Lena stood at her window, lost in thought as she watched the day give way to night."

# print(len(story))
# print(story.count(she))
# print(story.endswith("night"))
# print(story.count(watched))
# print(story.capitalize())
# print(story.find("village"))
print(story.replace("Lena","Mita"))

letter = '''Dear <|NAME|>,
You are selected!

Date: <|DATE|>
'''

name = input ("Enter Your Name\n")
date = input ("Enter Date\n")
letter= letter.replace("<|NAME|>", name)
letter= letter.replace("<|DATE|>", date)
print(letter)