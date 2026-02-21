# Number System Functions Program

def decimal_to_binary(num):
    return bin(num)[2:]

def decimal_to_octal(num):
    return oct(num)[2:]

def decimal_to_hexadecimal(num):
    return hex(num)[2:].upper()

def binary_to_decimal(binary):
    return int(binary, 2)


def main():
    while True:
        print("\n--- Number System Converter ---")
        print("1. Decimal to Binary")
        print("2. Decimal to Octal")
        print("3. Decimal to Hexadecimal")
        print("4. Binary to Decimal")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "5":
            print("Exiting program...")
            break

        elif choice == "1":
            num = int(input("Enter decimal number: "))
            print("Binary:", decimal_to_binary(num))

        elif choice == "2":
            num = int(input("Enter decimal number: "))
            print("Octal:", decimal_to_octal(num))

        elif choice == "3":
            num = int(input("Enter decimal number: "))
            print("Hexadecimal:", decimal_to_hexadecimal(num))

        elif choice == "4":
            binary = input("Enter binary number: ")
            print("Decimal:", binary_to_decimal(binary))

        else:
            print("Invalid choice. Please select 1-5.")


# Run program
main()