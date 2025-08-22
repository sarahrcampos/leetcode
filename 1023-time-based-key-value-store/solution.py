class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
       # print(self.map)
        if key not in self.map:
            return ""
                
        l, r = 0, len(self.map[key]) - 1
        while l <= r:
            m = (l+r) // 2
            t, value = self.map[key][m]
            if t == timestamp:
                return value
            if t < timestamp:
                l = m + 1
            else:
                r = m - 1
        
        return self.map[key][r][1] if r >= 0 and self.map[key][r][0] < timestamp else ""

#   
#[1,2,4,5]
#target = 3
            


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)


#time-based
#key-value
#múltiplos valores pra mesma chave
#recuperar o valor da chave num timestamp específico, tipo timeMap.get("foo", 3)
#se tiver vários, deve voltar o que tiver o maior tempo
#se nn tiver, é ""


#os timestamps que vao ser enviados no set são SEMPRE em ordem CRESCENTE


