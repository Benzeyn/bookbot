import sys

def main(book):
    with open(book) as f:
        book_file = book.split("/")[1]
        book_title = book_file.split(".")[0]
        full_text = f.read()
        single_string = ''.join(full_text.split()).lower()
        word_count_result = word_count(full_text)
        char_count_result = char_count(single_string)
        print_report(book_title.capitalize(), word_count_result, char_count_result)
        return 0

def word_count(string):
    return len(string.split())

def char_count(string):
    letter_count = {}
    for char in string:
        if char in letter_count:
            letter_count[char] += 1
        else:
            letter_count[char] = 1
    return letter_count

def print_report(book_title, word_count, char_count):
    print(f"====Report for {book_title}====")
    print()
    print(f"{book_title} contains {word_count} words.")
    print()
    for char in char_count:
        if char.isalpha():
            print(f"The '{char}' character was found {char_count[char]} times.")
    print()
    print("====End of report====")

main(sys.argv[1])