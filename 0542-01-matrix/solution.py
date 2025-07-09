#"sharing a common edge" = 4 directions
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(mat), len(mat[0])
        res = [[-1] * COLS for _ in range(ROWS)]
        directions = [[0,1], [1,0], [0,-1],[-1,0]]

        queue = deque()
        for i in range(ROWS):
            for j in range(COLS):
                if mat[i][j] == 0:
                    queue.append((i,j))
                    res[i][j] = 0
        
        distance = 1
        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for di, dj in directions:
                    newi,newj = i+di, j+dj
                    if newi in range(0,ROWS) and newj in range(0,COLS) and res[newi][newj] == -1:
                        queue.append((newi, newj))
                        res[newi][newj] = distance
            distance += 1
        return res
