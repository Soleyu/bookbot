import os

def main():
    book_path = get_book()
    text = get_text(book_path)
    number_of_words = get_number_words(text)
    character_number = character_count(text)
    print_report(number_of_words, character_number, book_path[6:-4])

def character_count(text):
    formated_text = text.lower()
    character_count= {}
    for char in formated_text:
        if char.isalpha():
            character_count[char] = character_count.get(char, 0) + 1


    sorted_count = dict(sorted(character_count.items()))
    return sorted_count

        


def get_text(path):
    try:
        with open(path) as f:
            return f.read()
    except Exception:
        print("Please enter a valid number or book name")
        exit(1)  # The number 1 indicates an error occurred

def get_number_words(text):
    words = text.split()
    return len(words)

def print_report(words, character_dict, book):
    title = f"--- This is the report for the book {book} ---"
    words_line = f"The book had a total of {words} words"
    print_text = title + "\n" + words_line + "\n" + "\n" + "\n"
    for item in character_dict:
        print_text += f"The letter {item} appeared a total of {character_dict[item]} times" + "\n"
    print(print_text) 

def get_book():
    files = os.listdir("books")
    book_list_print = ""
    book_options = []
    book_count = 0
    selected_book = "books/"
    if files == []:
        print("There are no books in the book folder please add some in simple text" + "\n")
    else:
        print("These are the books available to process: \n \n")
        for file in files:
            book = file[:-4]
            book_count += 1
            book_list_print += f"{book_count}.- "
            book_list_print += book + "\n" + "\n"
            book_options.append(file)
        print(book_list_print)

        choice = input("Choose a book (You can choose with either the name or the number)")
        if choice.isalpha():
            selected_book += choice + ".txt"
        else:
            choice = int(choice[0:]) - 1
            if choice > len(book_options) - 1:
                print("No such option")
                exit()
            else:
                choice_match = book_options[choice]
                selected_book += choice_match



    return selected_book


main()