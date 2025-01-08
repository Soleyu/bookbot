def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    number_of_words = get_number_words(text)
    character_number = character_count(text)
    print_report(number_of_words, character_number, book_path[6:-4])

def character_count(text):
    formated_text = text.lower()
    #non_characters = set()
    #non_characters = {"[", "]",  '_', ",", '"', "'", ".", "\n", " ", "?", "1", "2", "3", "4", "5", "6", "7", "8","9", "0", "(", ")", "#", ":", "-", "*", ";", "!", "%", "/", "@", "$"}
    #character_set = set()
    character_count= {}
    for char in formated_text:
        if char.isalpha():
            character_count[char] = character_count.get(char, 0) + 1


    sorted_count = dict(sorted(character_count.items()))
    return sorted_count

        


def get_text(path):
        with open(path) as f:
            return f.read()

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



main()