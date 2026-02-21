# Question 11 - Number Pattern Printer

rows = int(input("Enter number of rows: "))

#for loops

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()  # move to next line