class Solution(object):
    def islandPerimeter(self, grid):
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()

        def dfs(old_i, old_j, new_i, new_j):
            out_of_bounds = new_i >= ROWS or new_j >= COLS or new_i < 0 or new_j < 0
            if (grid[old_i][old_j] and (out_of_bounds or not grid[new_i][new_j])):
                print(old_i, old_j, new_i, new_j)
                return 1
            if out_of_bounds:
                return 0
            
            if (new_i, new_j) in visited:
                return 0
            visited.add((new_i, new_j))
            perim = dfs(new_i, new_j, new_i, new_j - 1)
            perim += dfs(new_i, new_j, new_i, new_j + 1)
            perim += dfs(new_i, new_j, new_i - 1, new_j)
            perim += dfs(new_i, new_j, new_i + 1, new_j)
            return perim
        return dfs(0,0,0,0)
        
