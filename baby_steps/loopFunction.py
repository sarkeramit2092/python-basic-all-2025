import time

numbers = [1,3,5,7,9,11,13,15]

def numbers_exit():
  for number in numbers:
    if number == "7":
        print(number)
        print ("Number 7 reached will exit loop now")
  end_of_loop ()

def end_of_loop():
  print("waiting......")
  time.sleep(1)
  print("You reached number 7")
  end_program ()

def end_program():
  time.sleep(2)
  print("program is shutting down")
  quit()


numbers_exit()