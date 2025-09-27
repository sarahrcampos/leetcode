#[1,2,3,4]
#[1,2,2,3,4]

#5,6,1,1,2,9, 10
#1,1,2,5,6,9,10
#smallestSide = [1, 1, 2, 3, 3] -- maxHeap
#biggestSide = [4, 6, 9, 10] --minHeap
#at each side I want to have n//2 or one side with n//2 and the other with n//2 + 1
#they can differ by at most 1 element
#n = len(smallestSide) + len(biggestSide)

class MedianFinder:

    def __init__(self):
        self.smallestSide = [] #maxHeap
        self.biggestSide = [] #minHeap
#1, 2
#smallest = [-1]
#biggest = [2]
    def addNum(self, num: int) -> None:
        if self.biggestSide and num >= self.biggestSide[0]:
            heapq.heappush(self.biggestSide, num)
        else:
            heapq.heappush(self.smallestSide, -num)
        
        if len(self.biggestSide) > len(self.smallestSide) + 1:
            smallest = heapq.heappop(self.biggestSide)
            heapq.heappush(self.smallestSide, -smallest)
        elif len(self.smallestSide) > len(self.biggestSide) + 1:
            biggest = heapq.heappop(self.smallestSide)
            heapq.heappush(self.biggestSide, -biggest)

    def findMedian(self) -> float:
        n = len(self.biggestSide) + len(self.smallestSide)
        if n % 2: #odd
            if len(self.biggestSide) > len(self.smallestSide):
                return self.biggestSide[0]
            return -self.smallestSide[0]
        else: #even
            return (self.biggestSide[0] - self.smallestSide[0])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
