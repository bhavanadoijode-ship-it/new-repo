# Question 17 - Palindrome Checker

text = input("Enter a word: ")

# Convert to lowercase
text = text.lower()

# Reverse the string
reversed_text = text[::-1]

if text == reversed_text:
    print("It is a Palindrome.")
else:
    print("It is not a Palindrome.")