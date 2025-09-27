class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        minPrice = [float("inf")] * n
        minPrice[src] = 0
        for _ in range(k + 1):
            tempMinPrice = minPrice.copy()
            for start, end, price in flights:
                tempMinPrice[end] = min(tempMinPrice[end], minPrice[start] + price)
            minPrice = tempMinPrice

        return minPrice[dst] if minPrice[dst] != float("inf") else -1
