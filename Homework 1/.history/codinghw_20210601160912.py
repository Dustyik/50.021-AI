WORDS = set(i.lower().strip() for i in open("words2.txt"))

def is_valid_word(word):
    return word in WORDS


#check if one char is different

#create graph using function