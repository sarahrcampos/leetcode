class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        count0, count1, count2 = 0, 0, 0
        for triplet in triplets:
            if triplet[0] == target[0] and triplet[1] <= target[1] and triplet[2] <= target[2]:
                count0 = 1
            if triplet[1] == target[1] and triplet[0] <= target[0] and triplet[2] <= target[2]:
                count1 = 1
            if triplet[2] == target[2] and triplet[0] <=target[0] and triplet[1] <= target[1]:
                count2 = 1
            if count0 and count1 and count2:
                return True
        return False
