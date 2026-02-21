# Question 10 - Simple ATM Simulator

balance = 5000

while True:
    print("\n--- ATM MENU ---")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        print("Current Balance:", balance)

    elif choice == "2":
        deposit = float(input("Enter amount to deposit: "))
        if deposit > 0:
            balance += deposit
            print("Deposit successful.")
        else:
            print("Invalid deposit amount.")

    elif choice == "3":
        withdraw = float(input("Enter amount to withdraw: "))
        if withdraw <= 0:
            print("Invalid withdrawal amount.")
        elif withdraw > balance:
            print("Insufficient balance.")
        else:
            balance -= withdraw
            print("Withdrawal successful.")

    elif choice == "4":
        print("Thank you for using the ATM.")
        break

    else:
        print("Invalid option. Please choose 1-4.")