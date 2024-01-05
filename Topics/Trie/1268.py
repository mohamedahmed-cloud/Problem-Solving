from typing import List
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = []


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        trie = TrieNode()

        for product in products:
            root = trie
            for chr in product:
                if chr in root.children:
                    root = root.children[chr]
                else:
                    root.children[chr] = TrieNode()
                    root = root.children[chr]
                root.word.append(product)

        # To show how the data store
        # print(trie.children.items())
        # def dfs(root):
        #     root = root.children.values()
        #     for i in root:
        #         print(i.children, i.word)
        #         dfs(i)
        # dfs(trie)

        res = []
        for chr in searchWord:
            trie = trie.children[chr]  if (trie and chr in trie.children) else None
            res.append(trie.word[:3] if trie else [])
        return res




slv = Solution()
products = ["mobile","mouse","moneypot","monitor","mousepad"]
searchWord = "mouse"
print(slv.suggestedProducts(products, searchWord))


# another solution

class TrieNode:
    def __init__(self):
        self.children = {}
        self.words = []
class Trie:

    def __init__(self):
        self.root = self.getNode()

    def getNode(self):
        return TrieNode()

    def insert(self, products: str) -> None:
        root = self.root
        for product in products:
            tmp = root
            for chr in product:
                if chr not in  root.children:
                    root.children[chr] = self.getNode()
                root = root.children[chr]
                root.words.append(product)
            root = tmp
        return root

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        products.sort()
        trie = trie.insert(products)
        res = []
        for chr in searchWord:
            trie = trie.children[chr] if trie and chr in trie.children else None
            res.append(trie.words[:3] if trie else [])
        return res

slv = Solution()
products = ["mobile","mouse","moneypot","monitor","mousepad"]
searchWord = "mouse"
print(slv.suggestedProducts(products, searchWord))
