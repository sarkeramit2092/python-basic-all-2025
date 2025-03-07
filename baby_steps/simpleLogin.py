user = "amit"
password = 1234

def login():
  print("Enter User Name and Password")
  entry1 = input("😵User Name: ")
  entry2 = int(input ("🤐Password: "))

  if entry1 == user and entry2 == password:
    print ("🤩 Access Granted!! 😎")
    logged_in()
  else:
    print("👻 Access Denied!! ☠️")

def logged_in():
  print("🫡 You Loggged in..... 😄")
  quit()

login()