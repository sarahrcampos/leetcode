class Solution(object):
    def decrypt(self, code, k):
        SIZE = len(code)
        result = [0] * SIZE
        if k == 0: return result
        start = 0 if k > 0 else SIZE - 1
        end = 0 if k > 0 else SIZE - 1
        substitute = 0
        while start < SIZE and start >= 0:
            substitute += code[end % SIZE]
            if end - start == k:
                substitute -= code[start]
                result[start] = substitute
                start = start + 1 if k > 0 else start - 1
            end = end + 1 if k > 0 else end - 1
        return result
        
