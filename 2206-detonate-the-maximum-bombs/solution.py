class Solution(object):
    #Time: O(n²)
    def maximumDetonation(self, bombs):
        #to know if (x,y) is inside a circle with the center in (a,b) and radius r
        #(x-a)² + (y-b)² <= r²
        canDetonate = {}

        #first: determine what are the bombs that the bomb at i can detonate
        for i in range(len(bombs)):
            a,b,r = bombs[i]
            for j in range(len(bombs)):
                if i == j:
                    continue
                x,y,r2 = bombs[j]
                if (x-a)**2 + (y-b)**2 <= r**2:
                    if i in canDetonate:
                        canDetonate[i].append(j)
                    else:
                        canDetonate[i] = [j]

        def dfs(i, detonated):
            if i in detonated:
                return 0
            current = 1
            detonated.add(i)
            if i in canDetonate:
                for bomb in canDetonate[i]:
                    current += dfs(bomb, detonated)
            return current
            
        maximum = 0
        for i in range(len(bombs)):
            current = dfs(i, set())
            maximum = max(maximum, current)
        return maximum
            



            #bfs:
            # current = 0
            # detonated = set() #keep track of which were already visited

            # queue = deque()
            # queue.append(i)

            # while queue:
            #     bomb = queue.popleft()
            #     if bomb in detonated:
            #         continue
            #     detonated.add(bomb)
            #     current += 1
            #     if bomb in canDetonate:
            #         queue.extend(canDetonate[bomb])

        
