import csv
import random

# The vocabulary set will consist of 95 ASCII printable characters and one
# unknown character (for denoting other characters not covered by this set).
CHARACTER_SET = [
    ' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.',
    '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=',
    '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
    'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[',
    '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
    'z', '{', '|', '}', '~', 'UNKNOWN'
]

CHARACTER_SET_SIZE = len(CHARACTER_SET)

# This function returns a dict that maps from characters to ID numbers.
def _build_vocab():
    return {k: v for v, k in enumerate(CHARACTER_SET)}

# Given a string, this function returns an array of ID numbers of the characters
# in the string.
def _string_to_character_ids(string, character_to_id):
    result = []
    for char in string:
        if char in CHARACTER_SET:
            result.append(character_to_id[char])
        else:
            result.append(character_to_id['UNKNOWN'])
    return result

def raw_data(file_path, ratio=0.90):
    character_to_id = _build_vocab()
    data = []
    with open(file_path, 'rb') as csvfile:
        urls_reader = csv.reader(csvfile)
        for row in urls_reader:
            x = _string_to_character_ids(row[0], character_to_id)
            y = 1 if row[1] == 'bad' else 0
            data.append((x, y))
    random.shuffle(data)
    split_index = int(float(len(data)) * ratio)
    train_data = data[0:split_index]
    test_data = data[split_index:]
    return train_data, test_data
