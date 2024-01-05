# Trie known as prefix tree or digital trees.


class TrieNode:
	def __init__(self):
		self.children = [None] * 26
		self.isEnd = False
class Trie:
	def __init__(self):
		self.root = self.getNode()

	def getNode(self):
		return TrieNode()
	
	def charToIndex(self, chr):
		return ord(chr) - ord("a")

	def insert(self, string):
		root = self.root
		n = len(string)
		for i in range(n):
			indx = self.charToIndex(string[i])
			if not root.children[indx]:
				root.children[indx] = self.getNode()
			root = root.children[indx]
		root.isEnd = True

	def search(self, string):
		n = len(string)
		root = self.root
		for i in range(n):
			indx = self.charToIndex(string[i])
			if not root.children[indx]:
				return False
			root = root.children[indx]
		return root.isEnd


def main():

	keys = ["the","a","there","anaswe","any",
			"by","their"]
	output = ["Not present in trie",
			"Present in trie"]

	t = Trie()

	for key in keys:
		t.insert(key)

	print("{} ---- {}".format("the",output[t.search("the")]))
	print("{} ---- {}".format("these",output[t.search("these")]))
	print("{} ---- {}".format("their",output[t.search("their")]))
	print("{} ---- {}".format("thaw",output[t.search("thaw")]))

if __name__ == '__main__':
	main()


