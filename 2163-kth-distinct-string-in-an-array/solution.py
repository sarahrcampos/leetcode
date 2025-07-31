class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        counter = defaultdict(int)
        for string in arr:
            counter[string] += 1
        for string in arr:
            if counter[string] == 1:
                k -= 1
                if not k:
                    return string
        return ""
