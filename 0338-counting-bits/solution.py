import math
class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0]
        currLog, head = 0, 0
        for i in range(1, n+1):
            if int(math.log(i, 2)) > currLog:
                currLog, head = int(math.log(i, 2)), i
                res.append(1)
                continue
            res.append(res[head] + (res[i-head] if head > 0 else 1))
        return res

        #O(nlogn):
        # res = []
        # for i in range(n+1):
        #     num = i
        #     count = 0
        #     while num > 0:
        #         count += num & 1
        #         num = num >> 1
        #     res.append(count)
        # return res
                
