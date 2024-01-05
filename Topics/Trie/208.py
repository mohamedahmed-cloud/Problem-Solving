class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False
class Trie:

    def __init__(self):
        self.root = self.getNode()

    def getNode(self):
        return TrieNode()

    def charToIndex(slef, chr):
        return ord(chr) - ord("a")

    def insert(self, word: str) -> None:
        n = len(word)
        root = self.root
        for i in range(n):
            indx = self.charToIndex(word[i])
            if not root.children[indx]:
                root.children[indx] = self.getNode()
            root = root.children[indx]
        root.isEnd = True

    def search(self, word: str) -> bool:
        n = len(word)
        root = self.root
        for i in range(n):
            indx = self.charToIndex(word[i])
            if not root.children[indx]: return False
            root = root.children[indx]
        return root.isEnd

    def startsWith(self, prefix: str) -> bool:
        n = len(prefix)
        root = self.root
        for i in range(n):
            indx = self.charToIndex(prefix[i])
            if not root.children[indx]: return False
            root = root.children[indx]
        return True


# Your Trie object will be instantiated and called as such:
obj = Trie()

obj.insert("word")
param_2 = obj.search("word")
param_3 = obj.startsWith("wo")
print(param_2)
print(param_3)
