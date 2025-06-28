#!/usr/bin/python3

def get_book_text(file_path):
    with open(file_path) as f:
        content = f.read()
        print(content)

def main():
    get_book_text("./books/frankenstein.txt")

main()
