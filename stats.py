def count_words(text):
    words = list(text.split())
    word_count = 0

    for  word in range(len(words)):
        word_count += 1
    
    return word_count


# Take the text from the book as a string
# Return the number of times each character (including symbols and spaces) appear in the string
    # Convert any character to lowercase
    # no duplicates
    # format: use a dict key string int value ({'p': 6121, 'r': 20818, 'o': 25225, ...})
    # import and call the function in main.py
        # capture result in a new variable
    # After printing word count, print dict and character count

def count_char(text):
    char_count = {}
    for char in text:
        char_count[char.lower()] = char_count.get(char.lower(),0) + 1
    return char_count

def sort_dictionary(dictionary):
    dict_list = []
    for key, value in dictionary.items():
        if key.isalpha():
            dict_list.append({"char":key,"num":value})
       
    sorted_list = sorted(dict_list, key=lambda x: x["num"], reverse=True)      
    return sorted_list