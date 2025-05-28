class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        a1, b1 = len(a)-1, len(b)-1
        ans = deque()
        while a1 >= 0 and b1 >= 0:
            current = int(a[a1]) + int(b[b1]) + carry
            carry = current//2
            ans.appendleft(str(current%2))
            a1,b1 = a1-1, b1-1
        while a1 >= 0:
            current = int(a[a1]) + carry
            carry = current//2
            ans.appendleft(str(current%2))
            a1 = a1-1
        while b1 >= 0:
            current = int(b[b1]) + carry
            carry = current//2
            ans.appendleft(str(current%2))
            b1 = b1-1
        if carry:
            ans.appendleft(str(carry))
        return "".join(ans)

