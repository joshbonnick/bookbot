def get_word_count(file_path):
    with open(file_path) as f:
        content = f.read()
        word_count = len(content.split());
        print(f"{word_count} words found in the document")
