# Question 4 - Age Calculator

birth_year = int(input("Enter your birth year: "))
current_year = int(input("Enter current year: "))

#validate input

if birth_year > current_year:
    print("Error! Birth year cannot be greater than current year.")
else:
    age = current_year - birth_year
    print("You are", age, "years old.")