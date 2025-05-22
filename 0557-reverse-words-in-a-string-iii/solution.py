class Solution(object):
    def reverseWords(self, s):
        array = list(s)
        l = 0
        for r in range(len(s)+1):
            if r == len(s) or s[r] == " ":
                i, j = l, r - 1
                while i < j:
                    array[i], array[j] = array[j], array[i]
                    i, j = i + 1, j - 1
                l = r + 1
        return "".join(array)
        
