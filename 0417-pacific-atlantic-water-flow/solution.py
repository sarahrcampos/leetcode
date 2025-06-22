#grid mxn
#pacific -> left and top
#atlantic -> right and bottom
#4 directions -> only if the value is <=
#output: lista de células que podem alcançar os dois oceanos
#começar pelas beiradas 
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pacific, atlantic = set(), set()
        for i in range(ROWS):
            pacific.add((i, 0))
            atlantic.add((i, COLS-1))
        for j in range(COLS):
            pacific.add((0, j))
            atlantic.add((ROWS-1, j))
        
        directions = [[0,1],[0,-1],[-1,0],[1,0]]
        def bfs(elements):
            visited = set()
            queue = deque(elements)
            while queue:
                for _ in range(len(queue)):
                    i, j = queue.popleft()
                    for di, dj in directions:
                        newi, newj = i + di, j + dj
                        if (newi in range(0,ROWS) and newj in range(0, COLS) and (newi, newj) not in elements and heights[newi][newj] >= heights[i][j]):
                            queue.append((newi, newj))
                            elements.add((newi, newj))
        bfs(pacific)
        bfs(atlantic)
        res = []
        for i, j in pacific:
            if (i, j) in atlantic:
                res.append([i,j])
        return res



