class TrieNode:
    def __init__(self):
        self.children = {}

class Trie:

    topCounter = 1

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        currentNode = self.root
        for c in word:
            if c in currentNode.children:
                currentNode = currentNode.children[c]
            else:
                newNode = TrieNode()
                currentNode.children[c] = newNode
                currentNode = newNode
        currentNode.children["*"] = self.topCounter
        self.topCounter += 1

    def search(self, word):
        currentNode = self.root
        for c in word:
            if c in currentNode.children:
                currentNode = currentNode.children[c]
            else:
                return None
        return currentNode

    def collectWords(self, node, word, words):
        currenNode = node
        for c in currenNode.children:
            if c == "*":
                words.append(word)
            else:
                self.collectWords(currenNode.children[c], word + c, words)
        return words 

    def autocomplete(self, prefix):
        currentNode = self.search(prefix)
        if currentNode is None:
            return None
        return self.collectWords(currentNode, prefix, [])[0:3]

t = Trie()
t.insert('cat')
t.insert('came')
t.insert('coming')
t.insert('cost')
t.insert('cold')
t.insert('core')
t.insert('cores')
t.insert('catman')
t.insert('bar')
t.insert('band')
t.insert('bake')
t.insert('barist')
t.insert('barTender')

print(t.autocomplete("c"))