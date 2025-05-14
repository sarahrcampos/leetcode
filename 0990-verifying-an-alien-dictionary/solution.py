class Solution(object):
    def isAlienSorted(self, words, order):
        #O(n*t)
        alphabet = {value:index for index, value in enumerate(order)}
        for i in range(len(words)-1):
            word = words[i]
            next = words[i+1]
            for j in range(len(word)):
                if j >= len(next):
                    return False
                if word[j] != next[j]:
                    if alphabet[word[j]] < alphabet[next[j]]:
                        break
                    return False
        return True
        
