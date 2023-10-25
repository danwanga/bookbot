def count_words(file_contents):
    return len(file_contents.split())


def count_letters(file_contents):
    """
    This function takes the text from the book as a string, 
    and returns the number of times each character appears in the string. 
    Convert any uppercase letters to lowercase letters, we don't want duplicates.
    """

    file_contents = file_contents.lower()
    letter_counts = {}
    for letter in file_contents:
        if letter.isalpha():
            if letter not in letter_counts:
                letter_counts[letter] = 1
            else:
                letter_counts[letter] += 1

    # convert the dictionary to a list then sort it
    letter_counts = list(letter_counts.items())
    letter_counts.sort(key=lambda x: x[1], reverse=True)

    # print the list in the format: "The 'e' character was found 46043 times"
    for letter, count in letter_counts:
        print(f"The '{letter}' character was found {count} times")

    return '--- End report ---'


with open("books/frankenstein.txt") as f:
    file_contents = f.read()

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count_words(file_contents)} words found in the document")
    print(count_letters(file_contents))
