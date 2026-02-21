# Question 19 - Text Analysis Functions

def count_characters(text):
    return len(text)


def count_words(text):
    words = text.split()
    return len(words)


def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count


def count_consonants(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char.isalpha() and char not in vowels:
            count += 1
    return count


def count_digits(text):
    count = 0
    for char in text:
        if char.isdigit():
            count += 1
    return count


def main():
    text = input("Enter a sentence: ")

    print("\n--- Text Analysis ---")
    print("Total Characters:", count_characters(text))
    print("Total Words:", count_words(text))
    print("Vowels:", count_vowels(text))
    print("Consonants:", count_consonants(text))
    print("Digits:", count_digits(text))


# Run program
main()