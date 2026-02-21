# Question 6 - Grade Calculator

print("Enter marks for 5 subjects:")

sub1 = float(input("Subject 1: "))
sub2 = float(input("Subject 2: "))
sub3 = float(input("Subject 3: "))
sub4 = float(input("Subject 4: "))
sub5 = float(input("Subject 5: "))

# Check for invalid marks
if (sub1 < 0 or sub1 > 100 or
    sub2 < 0 or sub2 > 100 or
    sub3 < 0 or sub3 > 100 or
    sub4 < 0 or sub4 > 100 or
    sub5 < 0 or sub5 > 100):

    print("Error! Marks must be between 0 and 100.")

else:
    total = sub1 + sub2 + sub3 + sub4 + sub5
    average = total / 5

    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 50:
        grade = "C"
    else:
        grade = "Fail"

    print("Total Marks:", total)
    print("Average:", average)
    print("Grade:", grade)