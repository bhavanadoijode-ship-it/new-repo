# Question 8 - Leap Year Checker

year = int(input("Enter a year: "))

#condition checking for leap year

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a Leap Year.")
else:
    print(year, "is not a Leap Year.")