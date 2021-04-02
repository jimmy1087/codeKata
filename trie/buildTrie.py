class TrieNode(object):
    def __init__(self):
        self.children = {}

class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        currentNode = self.root
        for c in word:
            if c in currentNode.children:
                currentNode = currentNode.children[c]
            else:
                currentNode.children[c] = TrieNode()
                currentNode = currentNode.children[c]
        currentNode.children['*'] = None
    
    '''
    word: 'cat'
    root: {}
    root: {c: {}}
    root: {c: { a: {} } }
    root: {c: { a: { t: {} } } }
    root: {c: { a: { t: { *: {} } } } }  
    word: 'catman'
    root: {c: { a: { t: { *: {}, m: {} } } } }  
    root: {c: { a: { t: { *: {}, m: { a: {} } } } } }
    root: {c: { a: { t: { *: {}, m: { a: { n: {} } } } } } }
    root: {c: { a: { t: { *: {}, m: { a: { n: { *: {} } } } } } } }
    '''

    def search(self, word):
        currentNode = self.root
        for c in word:
            if c in currentNode.children:
                currentNode = currentNode.children[c]
            else:
                return False
        if '*' in currentNode.children:
            return True
        else:
            return False

t = Trie()
t.insert('cat')
t.insert('catman')
t.insert('bar')
t.insert('barTender')

print(t.search('rn'),'False')
print(t.search('ca'),'False')
print(t.search('car'),'False')
print(t.search('cat'),'True')
print(t.search('catm'),'False')  # word ending in catm does not exists!
t.insert('catm')                 # after inserting word catm
print(t.search('catm'),'True')   # It should exists