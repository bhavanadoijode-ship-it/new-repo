# Question 9 - Ticket Pricing System

age = int(input("Enter your age: "))

if age < 0:
    print("Invalid age entered.")

elif age < 5:
    price = 0

elif age <= 17:
    price = 10

elif age <= 59:
    price = 20

else:
    price = 12

    