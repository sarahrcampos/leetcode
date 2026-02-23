#1 - keep a hashmap, the key is a word sorted -> n*(klogk) where k = max length of a word (100)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for word in strs:
            key = "".join(sorted(word))
            groups[key].append(word)
        return list(groups.values())
        
