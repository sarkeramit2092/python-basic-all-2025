# Show balance, Deposit and Withdraw

def show_balance(balance):
  print (f"Yor Balance is ${balance:.2f}.")

def deposit():

  amount = float(input("Enter an amount to br deposited: "))

  if amount <0 :
    print ("That's not a valid amount.")
    return 0
  else:
    return amount 

def withdrow(balance):
  amount = float(input("Enter amount to be withdrawn: "))

  if amount > balance:
    print("Insufficient Funds")
    return 0
  elif amount < 0:
    print("Amount must be greater than 0")
  else:
    return amount

def main ():

  balance = 0
  is_running = True

  while is_running:
    print("Banking Program")
    print("1. Show Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. EXIT")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
      show_balance(balance)

    elif choice == "2":
      balance   += deposit()

    elif choice == "3":
      balance   -= withdrow(balance)

    elif choice == "4":
      is_running = False

    else:
      print("Not a Valid Choice!!")



  print ("Thank You for Banking with US!!")


if __name__ == "__main__":
  main ()
