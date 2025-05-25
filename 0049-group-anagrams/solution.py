"""
constraints
1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""

class Solution:
    #Time: O(n²logn)
    #Space: O(n)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        for word in strs:
            key = "".join(sorted(word)) #O(nlogn)
            if key not in map:
                map[key] = [word]
            else:
                map[key].append(word)
        return list(map.values())

# class Solution:
#     #Time: O(n²)
#     #Space: O(n)
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         map = defaultdict(list)
#         for word in strs: #O(n)
#             frequencyMap = [0] * 26
#             for c in word: #O(k)
#                 frequencyMap[ord(c)%ord('a')] += 1
#             map[tuple(frequencyMap)].append(word) #O(n)
#         return list(map.values())
