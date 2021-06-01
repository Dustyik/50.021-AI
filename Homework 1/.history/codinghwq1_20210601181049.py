WORDS = set(i.lower().strip() for i in open("words2.txt"))
from search import Problem, breadth_first_search


def is_valid_word(word):
    return word in WORDS

def oneCharacterDifference(word1, word2):
    if (word1 == word2):
        return False
    else:
        count = 0
        for i in range(len(word1)):
            if(word1[i] != word2[i]):
                count += 1
        return count == 1

class WordLadder(Problem):
    def __init__(self, beginWord, Word):

    def actions(self, state):
        return [w for w in WORDS if one_char_away(w,state)]

    def result(self, state, action):
        return action