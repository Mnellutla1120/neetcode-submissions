class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
         tree.append(word)


    def search(self, word: str) -> bool:
        for i in range(len(tree)-1):
            if tree[i] == word:
                 return True
            else:
                 return False
        

    def startsWith(self, prefix: str) -> bool:
        for i in range(len(tree)-1):
            if tree[i].substr(0,len(prefix)) == prefix:
                 return True
            else:
                 return False
        
        
        
        