class Trie(object):

    def __init__(self):
        self.root = {}

    def insert(self, word):
        current = self.root
        for c in word:
            if c not in current:
                current[c] = {}
            current = current[c]
        current["."] = {}               
        

    def search(self, word):
        current = self.root
        for c in word:
            if not c in current:
                return False
            current = current[c]
        return "." in current
        

    def startsWith(self, prefix):
        current = self.root
        for c in prefix:
            if not c in current:
                return False
            current = current[c]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
