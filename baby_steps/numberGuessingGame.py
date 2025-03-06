# It is used to import the randint function from Python’s built-in random module.

# Purpose of randint

# randint(a, b) generates a random integer between a and b (both inclusive).

# In your case, randint(1, 3) is used to randomly pick a number between 1 and 3.

# Why from random import randint instead of import random?

# There are two ways to import and use randint:

# ✅ Using from random import randint (your method)

# from random import randint
# number = randint(1, 3)  # No need to prefix with 'random.'

# You can use randint() directly without needing to type random.randint().
# Cleaner and shorter code.
# ✅ Using import random

# import random

# number = random.randint(1, 3)  # Needs 'random.' prefix

from random import randint
import turtle

print("----- Guess The Number And Win A Mystery Prize -----")

def lucky_number():
    number = randint(1, 3)
    try:
        guess = int(input("Pick a number between 1 - 3: "))
        if guess not in [1, 2, 3]:  
            print("Invalid input! Choose a number between 1 and 3.")
            return lucky_number()
        if number 
            print("You Guessed Wrong!! The number was", number)
            booby_prize()
        else:
            print("You guessed correctly!! You win a prize!")
            your_prize()
    except ValueError:
        print("Invalid input! Please enter a number.")
        lucky_number()

def booby_prize():
    print("You get a poke in the eye!!" * 5)

def your_prize():
    t = turtle.Turtle()
    screen = turtle.Screen()
    screen.bgcolor("white")
    t.speed(3)
    t.pensize(3)
    t.color("red")

    t.begin_fill()
    t.left(50)
    t.forward(133)
    t.circle(50, 200)
    t.right(140)
    t.circle(50, 200)
    t.forward(133)
    t.end_fill()
    
    t.hideturtle()
    turtle.done()  # Keeps the turtle window open

lucky_number()


