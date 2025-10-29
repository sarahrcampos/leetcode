class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        i = 0
        res = []
        while i < len(words):
            line = []
            length = 0
            while i < len(words) and (length + len(words[i]) + len(line)) <= maxWidth:
                line.append(words[i])
                length += len(words[i])
                i += 1
            print(length)

            if i == len(words): #last line = left justify
                res.append(" ".join(line))
                for j in range(maxWidth - length - len(line) + 1):
                    res[-1] += " "
                return res
            
            spacesBetween = ""
            for j in range((maxWidth - length) // max(1, len(line) - 1)):
                spacesBetween += " "
            spacesLeft = (maxWidth - length) % max(1, len(line) - 1)
            
            for j in range(len(line)):
                if spacesLeft:
                    line[j] += " "                    
                    spacesLeft -= 1
                line[j] += (spacesBetween if (len(line) == 1 or j < len(line) - 1) else "" )
            res.append("".join(line))
        return res
            
