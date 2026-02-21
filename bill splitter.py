# Question 5 - Bill Splitter

total_bill = float(input("Enter total bill amount: "))
people = int(input("Enter number of people: "))
tip_percent = float(input("Enter tip percentage: "))

#validate input statements

if people <= 0:
    print("Error! Number of people must be greater than zero.")
else:
    tip_amount = (tip_percent / 100) * total_bill
    final_bill = total_bill + tip_amount
    amount_per_person = final_bill / people

    print("Total bill including tip:", final_bill)
    print("Each person should pay:", amount_per_person)