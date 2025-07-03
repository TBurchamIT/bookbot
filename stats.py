def get_num_words(book):
    word_count = len(book.split())
    return word_count

def count_characters(book):
    normalized = book.lower()
    letter_dictionary = {}
    for letter in normalized:
        if letter not in letter_dictionary:
            letter_dictionary[letter] = 1
        else:
            letter_dictionary[letter] += 1
    return letter_dictionary

def sort_dictionary(dictionary):
    result = []
    for key, value in dictionary.items():
        result.append({"char": key, "num": value})
    def sort_on(item):
        return item["num"]
    result.sort(reverse=True, key=sort_on)
    return result
