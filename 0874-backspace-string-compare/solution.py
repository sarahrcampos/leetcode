class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        p1, p2 = len(s)-1, len(t)-1
        while p1 >= 0 or p2 >= 0:
            skip = 0
            while p1 >= 0:
                if s[p1] == "#":
                    skip += 1
                else:
                    if skip == 0:
                        break
                    skip -= 1
                p1 -= 1

            skip = 0
            while p2 >= 0:
                if t[p2] == "#":
                    skip += 1
                else:
                    if skip == 0:
                        break
                    skip -= 1
                p2 -= 1

            if p1 >= 0 and p2 >= 0 and s[p1] != t[p2]:
                return False
            elif p1 < 0 and p2 < 0:
                return True
            elif p1 < 0 or p2 < 0:
                return False
            p1, p2 = p1-1, p2-1
        return True

