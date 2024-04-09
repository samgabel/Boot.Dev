def main():
    path = "books/frankenstein.txt"
    book_text = get_book_text(path)
    word_count = get_book_length(book_text)
    unique_char_count = get_char_count(book_text)
    char_list = get_each_char(unique_char_count)

    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words were found in the document")
    print()
    for char in char_list:
        print(f"The '{char["name"]}' was found {char["num"]} times ")
    print("--- End report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_book_length(text):
    words = text.split()
    return len(words)


def get_char_count(text):
    char_dict = {}
    converted = text.lower()
    for char in converted:
        if char not in char_dict:
            char_dict[char] = 0
        char_dict[char] += 1
    return char_dict


def sort_on(d):
    return d["num"]


def get_each_char(char_dict):
    char_list = []
    for item in char_dict:
        if item.isalpha():
            char_list.append({"name": item, "num": char_dict[item]})
    char_list.sort(reverse=True, key=sort_on)
    return char_list

#---------------------------------------------------------------

main()

