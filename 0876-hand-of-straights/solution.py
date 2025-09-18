class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        
        hand.sort()
        count = defaultdict(int)
        for num in hand:
            count[num] += 1

        for num in hand:
            if not count[num]:
                continue
            for j in range(groupSize):
                neighbor = num + j
                if not count[neighbor]:
                    return False
                count[neighbor] -= 1
        return True
            
