# Question 15 - Prime Number Checker

number = int(input("Enter a number: "))

if number <= 1:
    print(number, "is not a Prime Number.")

else:
    is_prime = True

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        print(number, "is a Prime Number.")
    else:
        print(number, "is not a Prime Number.")