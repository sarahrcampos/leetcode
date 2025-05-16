class Solution(object):
    def findChampion(self, n, edges):
        count = defaultdict(int) #é 0 se nn tem a chave
        for stronger, weaker in edges:
            count[weaker] += 1
        strongest = -1
        for i in range(n):
            if i not in count:
                if strongest > -1:
                    return -1
                strongest = i
        return strongest
