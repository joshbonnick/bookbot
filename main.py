#!/usr/bin/python3

import sys
from stats import *

def main(book_path):
    content = get_book_content(book_path);    
    word_count = get_word_count(content)
    character_count = list(get_char_count(content)).sort(reverse=True, key=str.lower)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")


main(sys.argv[1])
