def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

    print(f"--- Begin report of {book_path} ---")
    print(f"There are {num_words} words in the book.")
    print()
    

    for item in chars_sorted_list:
        print(f"The '{item['char']}' was found {item['num']} times.")

    print("--- End report ---")



def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(book_path):
    with open(book_path) as f:
        file_contents = f.read()
        return file_contents


def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(chars_dict):
    sorted_list = []
    for char in chars_dict:
        sorted_list.append({"char":char , "num":chars_dict[char]})
    sorted_list.sort(reverse = True, key = sort_on)
    return sorted_list



def get_chars_dict(text):
    text = text.lower()
    chars_dict = {}

    for char in text:
        if char.isalpha():
            if char in chars_dict:
                chars_dict[char] += 1
            else:
                chars_dict[char] = 1

    return chars_dict
    


main()


