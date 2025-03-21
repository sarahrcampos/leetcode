class Solution(object):
    def longestCommonPrefix(self, strs):
        first = strs[0]
        pointer = len(first)
        for s in strs[1:]:
            while (pointer > -1 and 
            (pointer > len(s) or first[:pointer] not in s[:pointer])):
                pointer -= 1
            if pointer == -1:
                return ""
        return first[:pointer]
