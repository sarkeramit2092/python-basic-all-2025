import time

name = []
addresses = []
jobs = []

def welcome_message():
  print ("Enter details into the database!!")
  enter_name()

def enter_name():
  entry1 = input("Enter Name: ").capitalize()
  name.append(entry1)
  enter_addresses()

def enter_addresses():
  entry2 = input ("Enter Address: ").capitalize()
  addresses.append(entry2)
  enter_job ()

def enter_job ():
  entry3 = input ("Enter Your Job Title: ").capitalize()
  jobs.append(entry3)
  show_details()

def show_details ():
  print ("Searching for Data......")
  print ("WAIT.......")
  time.sleep(3)
  print(name)
  print(addresses)
  print(jobs)
  clear_data()

def clear_data():
  print ("Delete details?")
  answer = input ("Yes/No: ")
  if answer.lower()==("yes" or "y"):
    name.clear()
    addresses.clear()
    jobs.clear()
    print("DELETED", name,addresses,jobs)
  else:
    print("You choose not to delete your info")
    quit()


welcome_message()
