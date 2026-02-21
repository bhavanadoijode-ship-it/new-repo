# Question 3 - String Manipulator

text = input("Enter a string: ")

# Convert cases
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())

# Length of string
print("Length:", len(text))

# Reverse string
print("Reversed:", text[::-1])

# Count vowels
vowels = "aeiouAEIOU"
count = 0

for char in text:
    if char in vowels:
        count += 1

print("Number of vowels:", count)