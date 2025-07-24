# --- The rest of your main.py file ---
from stats import count_words, count_char
# ...

def get_book_text(file):
    read_file = file.read()
    return read_file
        
def main():
    filepath = "books/frankenstein.txt"

    with open(filepath) as f:
        book_text = get_book_text(f)       
    num_words = count_words(book_text)

    
    char_count = count_char(book_text)
    #
    print(f'{num_words} words found in the document')
    print(char_count)

main()