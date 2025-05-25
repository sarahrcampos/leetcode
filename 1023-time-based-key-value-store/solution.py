class TimeMap(object):

    def __init__(self):
        self.map = {}
        

    def set(self, key, value, timestamp):
        if key not in self.map:
            self.map[key] = [[timestamp, value]]
            return
        
        self.map[key].append([timestamp, value])
        

    def get(self, key, timestamp):
        if key not in self.map:
            return ""
        
        valueList = self.map[key]
        l, r = 0, len(valueList)-1
        while l <= r:
            m = (l + r)//2
            if timestamp == valueList[m][0]:
                return valueList[m][1]
            elif timestamp > valueList[m][0]:
                l = m + 1
            else:
                r = r - 1
        if r >= 0:
            return valueList[r][1]
        return ""
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
