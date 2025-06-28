#!/usr/bin/python3

import sys
from stats import *

def main(book_path):
    content = get_book_content(book_path);    
    word_count = get_word_count(content)
    character_count = get_char_count(content)
    sorted_character_count = get_sorted_char_count(character_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for c in sorted_character_count:
        if(not c["char"].isalpha()):
            continue

        print(c["char"] + ': ' + str(c["num"]));

    print("============= END ===============")

book_path = None

if(len(sys.argv) > 1):
    book_path = sys.argv[1]
else:
    book_path = 'books/frankenstein.txt'

main(book_path)
