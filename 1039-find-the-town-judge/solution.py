class Solution(object):
    def findJudge(self, n, trust):
        count = [ [0] * 2 for i in range(n)]
        for i in range(len(trust)):
            a, b = trust[i]
            count[a-1][0] += 1
            count[b-1][1] += 1
        for i in range(0, n):
            trusts, trustedBy = count[i]
            if trusts == 0 and trustedBy == n - 1:
                return i + 1

        return -1
                
        
