class WordDictionary:

    def __init__(self):
        self.hashmap = {}

    def addWord(self, word: str) -> None:
        hashmap = self.hashmap
        for c in word:
            if c not in hashmap:
                hashmap[c] = {}
            hashmap = hashmap[c]
        hashmap["#"] = True #end of word

    def search(self, word: str) -> bool:
        def dfs(i, hashmap):
            if i == len(word):
                return "#" in hashmap            
            if word[i] == ".":
                for key in hashmap.keys():
                    if key != "#" and dfs(i+1, hashmap[key]):
                        return True
                return False
            elif word[i] not in hashmap:
                return False
            return dfs(i+1, hashmap[word[i]])
        return dfs(0, self.hashmap)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
