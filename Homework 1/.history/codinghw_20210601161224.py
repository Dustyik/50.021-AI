WORDS = set(i.lower().strip() for i in open("words2.txt"))

def is_valid_word(word):
    return word in WORDS


#check if one char is different
def oneCharacterDifference(word1, word2):
    if (word1 == word2):
        return False
    else:
        count = 0
        for i in range(len(word1)):
            if(word1[i] != word2[i]):
                count += 1
        return count == 1

#create graph using function
graph = defaultdictionary(set)

#BFS queue

#if we can endWOrd than return #step