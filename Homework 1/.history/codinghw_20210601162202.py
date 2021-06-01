WORDS = set(i.lower().strip() for i in open("words2.txt"))
from collections import defaultdict, deque

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
def createGraph(wordList, beginWord):
    graph = defaultdict(set)
    full_list = wordList + [beginWord]
    for word1 in full_list:
        for word2 in full_list:
            if oneCharacterDifference(word1, word2):
                graph[word1].add(word2)


    q = deque([(beginWord, 0)])
    visited = set()
    
    #BFS queue
    while q:
        node, step = q.popleft()

    #if we can endWOrd than return #step