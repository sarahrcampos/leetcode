class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        found0 = found1 = found2 = False 
        for triplet in triplets:            
            found0 |= (triplet[0] == target[0] and triplet[1] <= target[1] and triplet[2] <= target[2])                
            found1 |= (triplet[1] == target[1] and triplet[0] <= target[0] and triplet[2] <= target[2])                
            found2 |= (triplet[2] == target[2] and triplet[0] <= target[0] and triplet[1] <= target[1])                
            if found0 and found1 and found2:
                return True
        return False
            
