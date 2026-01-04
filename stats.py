def get_number_words(text):
    words = text.split()
    return len(words)

def character_count_sorted(text, sorttype):
    formated_text = text.lower()
    character_count= {}
    for char in formated_text:
        if char.isalpha():
            character_count[char] = character_count.get(char, 0) + 1

    if sorttype == "a":
        sorted_count = dict(sorted(character_count.items()))
        return sorted_count
    elif sorttype == "n":
        sorted_count = dict(sorted(character_count.items(), key=lambda x: x[1], reverse=True))
        return sorted_count

def character_count(text):
    formated_text = text.lower()
    character_count= {}
    for char in formated_text:
        if char.isalpha():
            character_count[char] = character_count.get(char, 0) + 1
    final_count = dict((character_count.items()))
    return final_count

