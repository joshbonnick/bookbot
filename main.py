#!/usr/bin/python3

from stats import *

def main():
    content = get_book_content("./books/frankenstein.txt");    
    get_word_count("./books/frankenstein.txt")
    print(get_char_count(content))
    

main()
