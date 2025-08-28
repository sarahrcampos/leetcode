#transform
#beginWord -> endWord
#wordList -> lista de palavras
#pra chegar em endWord, trocar 1 caractere no máximo
    #a posição importa!
#beginWord nn ta na wordList
#retorno: número de palavras na transformação mais curta (ou 0 se nn for possível)

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        #generate patterns for all words in wordList
        wordList.append(beginWord)    #append beginWord to wordList to generate the patterns for beginWord    
        pattern2Word, word2Pattern = defaultdict(set), defaultdict(set)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                pattern2Word[pattern].add(word)
                word2Pattern[word].add(pattern)        
        if not word2Pattern[endWord]:
            return 0

        visitedWords = set([beginWord])
        queue = deque([beginWord])
        length = 1            
        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return length
                for pattern in word2Pattern[word]:
                    for word in pattern2Word[pattern]:
                        if word not in visitedWords:
                            visitedWords.add(word)
                            queue.append(word)
            length += 1
        
        return 0
