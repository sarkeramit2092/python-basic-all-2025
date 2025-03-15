import time

def countdown_timer():
  try:
    seconds = int(input("Enter the contdown time in seconds: "))
    while seconds > 0:
      print (f"Time remaining : {seconds} seconds")
      time.sleep(1)
      seconds-=1
    print("TIME's UP!!")
  except ValueError:
    print("Invalid Input!!")

countdown_timer()