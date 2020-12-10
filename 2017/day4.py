def is_valid(passphrase):
    phrase_elements = passphrase.split()

    for a_index, a in enumerate(phrase_elements):
        for b_index, b in enumerate(phrase_elements):
            if a_index != b_index and a == b:
                return False
    return True


def has_anagram(passphrase):
    phrase_elements = passphrase.split()

    for a_index, a in enumerate(phrase_elements):
        for b_index, b in enumerate(phrase_elements):
            if a_index != b_index and is_anagram(a, b):
                return True
    return False


def is_anagram(element_a, element_b):
    element_a_chars = list(element_a)
    element_b_chars = list(element_b)

    for index_a, char_a in enumerate(element_a_chars):
        if char_a in element_b_chars:
            index_b = element_b_chars.index(char_a)
            del element_b_chars[index_b]
        else:
            return False

    return len(element_b_chars) == 0


# assert has_anagram("oiii ioii iioi iiio") == False, "Has an anagram"

with open('day4/input.txt', 'r') as content_file:
    total = 0
    for row in content_file.readlines():
        total += 1 if not has_anagram(row) else 0
    print total
