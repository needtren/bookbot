def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_word_count(text)
    num_letters = get_letter_count(text)
    num_letters_sorted = sort_dict(num_letters)
    print (f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()
    for letter, count in num_letters_sorted.items():
        print(f"The '{letter}' character was found {count} times")
    print("--- End report ---")

def get_word_count(text):
    words = text.split()
    return len(words)

def get_letter_count(text):
    letter_dict = {}
    text_lowercase = text.lower()
    for letter in text_lowercase:
        if letter.isalpha():
            if letter in letter_dict:
                letter_dict[letter] += 1
            else:
                letter_dict[letter] = 1

    return letter_dict

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def sort_dict(letter_dict):
    sorted_dict = dict(sorted(letter_dict.items(), key=lambda item: item[1], reverse=True))
    return sorted_dict

main()