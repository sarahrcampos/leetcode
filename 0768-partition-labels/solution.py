class Solution:
    #Time: O(nlogn)
    #Space: O(n)
    def partitionLabels(self, s: str) -> List[int]:
        letters = {}
        #marcar primeira e última aparição de cada letra
        for i in range(len(s)):
            if s[i] not in letters:
                letters[s[i]] = [i, i]
            else:
                letters[s[i]][1] = i
        #merge overlapping intervals
        aux = list(letters.values())
        aux.sort()
        current = aux[0]
        res = []
        for i in range(1, len(aux)): 
            if current[1] < aux[i][0]:
                res.append(current[1] - current[0] + 1)
                current = aux[i]
            else:
                current[1] = max(current[1], aux[i][1])
        res.append(current[1] - current[0] + 1)
        return res
                
