def get_book_content(file_path):
    with open(file_path) as f:
        return f.read()

def get_word_count(file_path):
    content = get_book_content(file_path)
    word_count = len(content.split());
    print(f"{word_count} words found in the document")


def get_char_count(content):
    character_map = {};
    for c in content:
        c = c.lower()
        if(c not in character_map):
            character_map[c] = 0;
        character_map[c] += 1;

    return character_map
