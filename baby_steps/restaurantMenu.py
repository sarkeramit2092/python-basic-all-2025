import time

def hello_message():
  print("Welcome to My Pizza Restaurant.")
  print("We are here to take Your Order.")
  pizza_topping()

def pizza_topping():
  toppings = ["mushrooms","onions","chicken"]
  request = input("Please enter a topping: ")
  if request in toppings:
    print(request,"are Avaiable.")
    soft_drinks()
  else:
    print(("Processing.........."))
    time.sleep(3)
    print(request,"Sorry not Available.")
    quit()

def soft_drinks():
  print("please Order Your Drinks!!")
  drinks = ["cola","juice","coffee"]
  request = input("Enter Your Drink: ")
  if request in drinks:
    print(request, "is Available!!")
    thank_customer()
  else:
    print("Processing........")
    print(request,"is not currently available here!!")
    time.sleep(3)
    print(request, "is not currently available here!!")

def thank_customer():
  print("Enjoy Your Meal!!")

hello_message()