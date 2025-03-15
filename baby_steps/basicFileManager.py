import os

print("==============")
print("File Manager")
print("==============")

def control():
  print("1. Open Folder")
  print("2. Open File")
  print("3. Exit")

  choice = input (">>")
  if choice == "1":
    open_folder()
  elif choice == "2":
    open_files()
  elif choice == "3":
    print ("Bye")
    quit()
  else:
    print("Wrong Input.")

def open_folder():
  path = input("c:\\ ")
  os.chdir(path)
  os.startfile(path)

def open_files():
  path = input("c:\\ ")
  os.chdir(path)

  for file in os.listdir(path):
    print(file)
  filename = input("Enter Filename: ")
  if os.path.exists(filename) and filename.endswith(".txt"):
    with open (filename, "r") as f:
      contents = f.read()
      print(contents)
  else:
    print("Error Occured!!")

control()