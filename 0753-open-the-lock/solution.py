class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        queue = deque([target])
        visited = set([target])
        deadends = set(deadends)  

        moves = 0
        while queue:
            for _ in range(len(queue)):
                current = queue.popleft()
                if current == "0000":
                    return moves
                #put neighbors in queue
                for i in range(4):
                    digit = int(current[i])
                    up = current[:i] + str(digit + 1 if digit+1 < 10 else 0) + current[i+1:]
                    down = current[:i] + str(digit - 1 if digit - 1 > -1 else 9)  + current[i+1:]

                    if up not in visited and up not in deadends:
                        queue.append(up)
                        visited.add(up)
                    if down not in visited and down not in deadends:
                        queue.append(down)
                        visited.add(down)
            moves += 1
        return -1

