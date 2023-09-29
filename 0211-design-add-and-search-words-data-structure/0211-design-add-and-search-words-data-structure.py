class Trie:
    def __init__(self):
        self.endOf = False
        self.children = {}
class WordDictionary:

    def __init__(self):
        self.root = Trie()          

    def addWord(self, word: str) -> None:        
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = Trie()
            curr = curr.children[c]
        curr.endOf = True
             

        

    def search(self, word: str) -> bool:
        
        def dfs(index,root):
            curr = root
            for i in range(index,len(word)):
                c = word[i]
                if c  == '.':                           
                    for child in curr.children.values():
                        if dfs(i+1,child):
                            return True
                    return False
                    
                else :
                    if c not in curr.children:
                        return False
                    curr = curr.children[c]                
            return curr.endOf
        return dfs(0,self.root)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)