class Trie:
    def __init__(self):
        self.hashmap = {}

    def insert(self, word: str) -> None:
        hashmap = self.hashmap
        for i in range(len(word)):
            if word[i] not in hashmap:
                hashmap[word[i]] = {}
            hashmap = hashmap[word[i]]
        hashmap["."] = "." #end of word
    def search(self, word: str) -> bool:
        hashmap = self.hashmap
        for i in range(len(word)):
            if word[i] not in hashmap:
                return False
            hashmap = hashmap[word[i]]
        return "." in hashmap

    def startsWith(self, prefix: str) -> bool:
        hashmap = self.hashmap
        for i in range(len(prefix)):
            if prefix[i] not in hashmap:
                return False
            hashmap = hashmap[prefix[i]]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
