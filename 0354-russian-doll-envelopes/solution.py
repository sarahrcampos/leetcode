#[width, height]
#if width_x < width_y and height_x < height_y: x can fit in y
#return: maximum number of envelopes that you can russian doll

#[[5,4],[6,4],[6,7],[2,3]]
#[2,3] => [5,4] => [6,7]

#[2,3], [5,6], [5,4], [6,7]

#DP + Binary Search -> T: O(nlogn) S:O(n)
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key = lambda x: (x[0], -x[1]))
        russianDoll = [float("-inf")]
        for width, height in envelopes:
            if height > russianDoll[-1]:
                russianDoll.append(height)
            else:
                l, r = 0, len(russianDoll) - 1
                while l < r:
                    m = (l + r)//2
                    if height > russianDoll[m]:
                        l = m + 1
                    else:
                        r = m
                russianDoll[r] = height

        return len(russianDoll) - 1
