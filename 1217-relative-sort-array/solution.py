class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        counter = defaultdict(int)
        for num in arr1:
            counter[num] += 1
        res = []
        for num in arr2:
            for _ in range(counter[num]):
                res.append(num)
            del counter[num]
        
        keys = list(counter.keys())
        keys.sort()
        for key in keys:
            for _ in range(counter[key]):
                res.append(key)
        
        return res
            

