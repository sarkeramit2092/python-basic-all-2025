age = int(input("Enter Your Age: "))

if age < 13:
    print ("You are a Child.")
elif 13< age <19:
    print ("Teenager")
elif 20< age <59:
    print ("Adult")
elif age > 60:
    print ("Senior")
else:
    print ("wrong input!!")