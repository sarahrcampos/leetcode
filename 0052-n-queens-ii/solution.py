class Solution:
    def totalNQueens(self, n: int) -> int:
        cols = [False] * n
        positive_diag = defaultdict(bool)
        negative_diag = defaultdict(bool)
        solutions = 0

        def backtrack(i):
            nonlocal solutions
            if i == n:
                solutions += 1
                return
            
            for j in range(n):
                if cols[j] or positive_diag[i + j] or negative_diag[i - j]:
                    continue
                cols[j] = True
                positive_diag[i + j] = True
                negative_diag[i - j] = True
                backtrack(i + 1)
                cols[j] = False
                positive_diag[i + j] = False
                negative_diag[i - j] = False
            
        backtrack(0)
        return solutions

