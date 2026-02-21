# Question 13 - Sum and Average Calculator

count = int(input("How many numbers do you want to enter? "))

total = 0

for i in range(count):
    num = float(input("Enter number: "))
    total += num

if count > 0:
    average = total / count
    print("Sum:", total)
    print("Average:", average)
else:
    print("Cannot calculate average with zero numbers.")