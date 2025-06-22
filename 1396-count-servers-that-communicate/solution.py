#grid mxn
# 1 = tem server, 0 = nao tem
#2 servidores comunicam se eles estão na mesma linha ou coluna
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        count_rows, count_cols = defaultdict(int), defaultdict(int)
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    count_rows[i] += 1
                    count_cols[j] += 1
        res = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] and (count_rows[i] > 1 or count_cols[j] > 1):
                    res += 1
        
        return res
        

