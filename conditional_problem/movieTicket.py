def ticketPrice():
    age = int(input("Enter your age: "))

    if age < 18:
        print ("Your ticket price is $8!!")
        getDiscount()
    else:
        print ("Your ticket price is $12!!")
        getDiscount()

def getDiscount():
    day = input("Enter the Day you planning to watch movie: ")
    if day == "wednesday":
        print(f"You get $2 Discount!!")
    else:
        (f"{day} -No Discount for Today!!")

ticketPrice()

# new way

age =26
day "wednesday"

price = 12 if age >= 18 else 8

if day == "wednesday":
    price -=2
print("Tickect price for you is $",price)   