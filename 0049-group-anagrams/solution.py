class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result, map = [], {}
        for s in strs:
            sortS = str(sorted(s))
            if sortS in map:
                result[map[sortS]].append(s)
            else:
                result.append([s])
                map[sortS] = len(result)-1
        return result
