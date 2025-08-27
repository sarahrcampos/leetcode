class Solution:    
    def addWord(self, trie, word):
        for c in word:
            if c not in trie:
                trie[c] = {}
            trie = trie[c]
        trie["#"] = True

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}
        for word in words:
            self.addWord(trie, word)
        ROWS, COLS = len(board), len(board[0])

        directions = [[0,-1],[0,1],[-1,0],[1,0]]
        res = []
        def dfs(i, j, curr, hashmap):            
            if (i < 0 or i >= ROWS or
                j < 0 or j >= COLS or
                board[i][j] == "#" or
                board[i][j] not in hashmap):
                return
            c = board[i][j]
            board[i][j] = "#" #visited
            curr.append(c)
            if "#" in hashmap[c]:
                del hashmap[c]["#"]
                res.append("".join(curr))
            for di, dj in directions:
                newI, newJ = i+di, j+dj
                dfs(newI, newJ, curr, hashmap[curr[-1]])
            board[i][j] = c
            curr.pop()

        for i in range(ROWS):
            for j in range(COLS):
                dfs(i,j,[],trie)
        
        return res
