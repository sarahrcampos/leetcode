#não pode ser do mesmo array
#brute force - O(n²)
class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        minimum, maximum = float("inf"), float("-inf")
        minIndex, maxIndex = -1, -1
        for i in range(len(arrays)):
            if arrays[i][0] < minimum:
                minIndex = i
                minimum = arrays[i][0]
            if arrays[i][-1] > maximum:
                maxIndex = i
                maximum = arrays[i][-1]
        
        distance = 0
        for i in range(len(arrays)):
            if i != minIndex:
                distance = max(distance, abs(arrays[i][-1] - minimum))
            if i != maxIndex:
                distance = max(distance, abs(arrays[i][0] - maximum))
        
        return distance
