WORDS = set(i.lower().strip() for i in open("words2.txt"))
from collections import defaultdict, deque

def is_valid_word(word):
    return word in WORDS

def createWordList(wordLength):
    word_list = []
    for word in WORDS:
        if len(word) == wordLength:
            word_list.append(word)
    return word_list

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
def createGraph(beginWord, endWord, wordList):
    graph = defaultdict(set)
    full_list = wordList + [beginWord]
    for word1 in full_list:
        for word2 in full_list:
            if oneCharacterDifference(word1, word2):
                graph[word1].add(word2)


    q = deque([(beginWord, 0)])
    visited = set()
    
    #BFS queue, if we can endWOrd than return #step
    while q:
        node, step = q.popleft()  
        if node == endWord:
            return step + 1  
        if node not in visited:
            visited.add(node)
            for next in graph[node]:
                if next not in visited:
                    q.append((next, step + 1))

def main():
    beginWord = "cars"
    endWord = "cats"
    wordList = createWordList(len(beginWord))
    createGraph(beginWord, endWord, wordList)

if __name__ == '__main__':
    main()