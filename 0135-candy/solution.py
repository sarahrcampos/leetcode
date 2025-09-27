# n children
# len(ratings) = n -> rating[i] is the rating of the ith child
# at least 1 to each child
#higher rating than their neighbor = more candy
#minimum number of candies 

#ratings: [1,0,2]
#candy:   [2,1,2] because 0 is less than its neighbors

#ratings: [1,2,2]
#candy:   [1,2,1] because the 3rd child has equal rating

#ratings: [5, 1, 4, 4, 6, 7, 8]
#candy:   [2, 1, 2, 1, 2, 3, 4]

#ratings: [5, 3, 2, 1]
#candy:   [4, 3, 2, 1] - ERRADO

#ratings: [1, 2, 1]
#pre:     [0, 1, 0]
#pos:     [0, 1, 0]

#ratings: [5, 3, 2, 1]
#pre:     [0, 0, 0, 0]
#pos:     [3, 2, 1, 0]

#ratings: [5, 1, 4, 4, 6, 7, 8]
#pre:     [1, 1, 2, 1, 2, 3, 4]
#pos:     [2, 1, 1, 1, 1, 1, 1]

#ratings: [5, 1, 4, 10, 6, 7, 8]
#pre:     [1, 1, 2, 3, 1, 2, 3]
#pos:     [2, 1, 1, 2, 1, 1, 1]
#max:     [2, 1, 2, 3, 1, 2, 3]


# if r[i] > r[i-1]: c[i] = 1 + c[i-1]
# if r[i] > r[i+1]: c[i] = 1 + c[i + 1]

class Solution:
    def candy(self, ratings: List[int]) -> int:
        preCandy = [1] * len(ratings)
        minCandy = posCandy = [1] * len(ratings)

        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                preCandy[i] += preCandy[i - 1]        
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                posCandy[i] += posCandy[i + 1]
        for i in range(len(ratings)):
            minCandy[i] = max(preCandy[i], posCandy[i])

        return sum(minCandy)
