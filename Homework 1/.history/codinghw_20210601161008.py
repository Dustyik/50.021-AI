WORDS = set(i.lower().strip() for i in open("words2.txt"))

def is_valid_word(word):
    return word in WORDS


#check if one char is different
def oneCharacterDifference(word1, word2):
    if (word1 == word2):
        return false

#create graph using function

#BFS queue

#if we can endWOrd than return #step