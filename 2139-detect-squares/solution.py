class DetectSquares:

    def __init__(self):
        self.points = defaultdict(lambda: defaultdict(int))

    def add(self, point: List[int]) -> None:
        x, y = point
        self.points[x][y] += 1        

    def count(self, point: List[int]) -> int:
        qx, qy = point
        if qx not in self.points:
            return 0
        
        squares = 0
        
        for py, pcounter in self.points[qx].items():
            if py == qy:
                continue
            length = abs(qy - py)

            #outros possíveis pontos:
            #(qx - length, qy)            
            #(qx - length, py)
            #ou
            #(qx + length, qy)
            #(qx + length, py)

            left = qx - length
            squares += pcounter * self.points[left][qy] * self.points[left][py]

            right = qx + length
            squares += pcounter * self.points[right][qy] * self.points[right][py]
        return squares
            
            

        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
