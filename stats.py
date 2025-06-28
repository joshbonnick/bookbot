def get_book_content(file_path):
    with open(file_path) as f:
        return f.read()

def get_word_count(content):
    word_count = len(content.split());
    return word_count

def get_char_count(content):
    character_map = {};
    for c in content:
        c = c.lower()
        if(c not in character_map):
            character_map[c] = 0;
        character_map[c] += 1;

    return character_map
