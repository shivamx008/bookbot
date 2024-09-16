


def read_the_book(path):
    with open(path) as f:
        return f.read()

def find_no_words(book):
    return len(book.split())

def count_chars(book):

    book =  book.lower()
    char_count = {}
    for c in book:
        char_count [c] = char_count.get(c,0) + 1
    return char_count

def list_of_dict(dictt):
    list_dictt = []
    for keyy in dictt:
        list_dictt.append({ "char" : keyy, "num" : dictt[keyy]})
    return list_dictt

def sort_on(dict):
    return dict["num"]

def main():
    book_path = "books/frankenstein.txt"
    textt = read_the_book(book_path)
    #print(textt)
    no_of_words = find_no_words(textt)
    #print(f"{no_of_words} is the number of words in this book")
    counted_chars = count_chars(textt)
    #print(f"the list of all the chars in the book and their occurances = {counted_chars}")
    list_dict = list_of_dict(counted_chars)
    
    list_dict.sort(reverse=True, key=sort_on)
    print (list_dict)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{no_of_words} words found in the document")
    print()
    for i in list_dict:
        if i["char"].isalpha():
            print(f"The '{i['char']}' character was found {i['num']} times")
    print("--- End report ---")


if __name__ == "__main__":
    main()