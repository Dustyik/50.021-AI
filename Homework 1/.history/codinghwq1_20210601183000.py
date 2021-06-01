WORDS = set(i.lower().strip() for i in open("words2.txt"))
from search import Problem, breadth_first_search


def is_valid_word(word):
    return word in WORDS

def oneCharacterDifference(word1, word2):
    if (len(word1) != len(word2)):
        return False
    else:
        count = 0
        for i in range(len(word1)):
            if(word1[i] != word2[i]):
                count += 1
        return count == 1

class WordLadder(Problem):
    def __init__(self, beginWord, endWord):
        super().__init__(beginWord, endWord) #extends init from the super class

    def actions(self, state):
        return_val = []
        for w in WORDS:
            if (oneCharacterDifference(w, state)):
                return_val.append(w)
        return return_val


    def result(self, state, action):
        return action

if __name__ == '__main__':
    wlp = WordLadder('best', 'math')
    solution = breadth_first_search(wlp)
    print('No solution' if solution is None else solution.solution())
