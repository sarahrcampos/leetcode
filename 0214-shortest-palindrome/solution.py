class Solution:
    def shortestPalindrome(self, s: str) -> str:
        def isPalindrome(word):
            #print(word)
            return word == word[::-1]
        curr = ""
        i = len(s) - 1

        while not isPalindrome(curr + s):
            curr = s[i:][::-1]
            i -= 1
        return curr + s
