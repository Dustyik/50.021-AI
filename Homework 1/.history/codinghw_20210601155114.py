WORDS = set(i.lower().strip() for i in open("words2.txt"))

def is_valid_word(word):
    return word in WORDS


print (is_valid_word("test"))