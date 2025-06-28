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

def get_sorted_char_count(count_dict):
    chars = [];
    for c in count_dict:
        chars.append({"char": c, "num": count_dict[c]})

    chars.sort(reverse=True, key=lambda c: c['num']);
    return chars
