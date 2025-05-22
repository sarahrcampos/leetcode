class Solution(object):
    #Time: O(n+m)
    #Space: O(n+m)
    def backspaceCompare(self, s, t):
        new_s, new_t = [], []
        for i in range(len(s)):
            if s[i] == "#" and new_s:
                new_s.pop()
            elif s[i] != "#":
                new_s.append(s[i])
        for j in range(len(t)):
            if t[j] == "#" and new_t:
                new_t.pop()
            elif t[j] != "#":
                new_t.append(t[j])
        return "".join(new_t) == "".join(new_s)

