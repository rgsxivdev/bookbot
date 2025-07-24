import sys
from stats import count_words, count_char, sort_dictionary


def get_book_text(file):
    read_file = file.read()
    return read_file
        
def main():
    if len(sys.argv) !=2:
        print("Usage: python3 main.py <path_to_book>")
    
    filepath = sys.argv[1]

    with open(filepath) as f:
        book_text = get_book_text(f)      

    num_words = count_words(book_text) 
    char_count = count_char(book_text)
    sorted_dictionary = sort_dictionary(char_count)

    #print(f'============ BOOKBOT ============')
    #print(f"Analyzing book found at books/frankenstein.txt...")
    #print(f'----------- Word Count ----------')
    print(f'Found {num_words} total words')
    
    
    for d in sorted_dictionary:
        print(f'{d["char"]}: {d["num"]}')
main()