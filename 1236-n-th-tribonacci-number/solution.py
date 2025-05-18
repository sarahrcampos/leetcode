class Solution(object):
    def tribonacci(self, n):
        cache = { 0: 0, 1:1, 2:1 }
        def tribo(i):
            if i not in cache:
                cache[i] = tribo(i-1) + tribo(i-2) + tribo(i-3)
            return cache[i]
        return tribo(n)
        
