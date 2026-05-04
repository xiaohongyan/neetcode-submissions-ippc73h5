class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]

        cur.isEnd = True
        

    def search(self, word: str) -> bool:
       cur = self.root
       
       def backTracking(i, cur):
            if i == len(word):
                return cur.isEnd

            c = word[i]
            if c in cur.children:
                cur = cur.children[c]
                return backTracking(i + 1, cur)
            elif c == '.':
                for child in cur.children:
                    if backTracking(i + 1, cur.children[child]):
                        return True
                return False
            else:
                return False
            
       return backTracking(0, cur)

        
