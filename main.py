import sys
import os
from stats import get_number_words
from stats import character_count

def main():
    print("Welcome to BookBOT \n")
    try:
        if len(sys.argv) == 2:
            book_path = sys.argv[1]
        else:
            book_path = get_book()
        text = get_text(book_path)
        number_of_words = get_number_words(text)
        sortype = type_sort()
        character_number = character_count(text, sortype)
        print_report(number_of_words, character_number, book_path[6:-4])

        return 0
    except ValueError as e:
        print(e)
        return 1

def type_sort():
    input_string = input("Would you like alphabetic sorting or numeric sorting of letters \n")
    input_string = input_string.lower()
    selection = input_string[0]
    if selection not in ("a", "n"):
        raise ValueError("Please choose a valid sorting method")
    else :
        return selection    

def get_text(path):
    try:
        with open(path) as f:
            return f.read()
    except FileNotFoundError:
        raise ValueError("Please enter a valid number or book name")

def print_report(words, character_dict, book):
    title = f"--- This is the report for the book {book} ---"
    words_line = f"The book had a total of {words} words"
    lines = [
        f"The letter {char} appeared a total of {count} times"
        for char, count in character_dict.items()
    ]
    print_text = title + "\n" + words_line + "\n\n" + "\n".join(lines) + "\n\nThanks for using BookBOT"
    print(print_text) 

def get_book():
    files = os.listdir("books")
    book_list_print = ""
    book_options = []
    book_count = 0
    selected_book = "books/"
    if files == []:
        raise ValueError("There are no books in the book folder please add some in simple text" + "\n")
    else:
        print("These are the books available to process: \n \n")
        for file in files:
            book = file[:-4]
            book_count += 1
            book_list_print += f"{book_count}.- "
            book_list_print += book + "\n" + "\n"
            book_options.append(file)
        print(book_list_print)

        choice = input("Choose a book (You can choose with either the name or the number) \n")
        if choice.isalpha():
            selected_book += choice + ".txt"
        else:
            if choice.isnumeric():
                choice = int(choice[0:]) - 1
                if choice > len(book_options) - 1:
                    raise ValueError("No such option")
                else:
                    choice_match = book_options[choice]
                    selected_book += choice_match
            else:
                raise ValueError("Please input a valid number")



    return selected_book

if __name__ == "__main__":
    sys.exit(main())
