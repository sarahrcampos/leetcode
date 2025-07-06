class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split()
        for i in range(1, len(words)):            
            if i-1 >= 0 and words[i][0] != words[i-1][-1]:
                return False
            if i+1 < len(words) and words[i][-1] != words[i+1][0]:
                return False
        
        return sentence[0] == sentence[-1]
