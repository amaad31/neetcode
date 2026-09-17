class TrieNode:
    def __init__(self, ch=None):
        self.nodeRecord = {}
        self.nodeChar = ch
        self.end = False

class PrefixTree:
    def __init__(self):
        self.dummy = TrieNode()

    def insert(self, word: str) -> None:
        curNode = self.dummy
        for curChar in word:
            if curChar in curNode.nodeRecord:
                curNode = curNode.nodeRecord[curChar]
                continue
            newTrieNode = TrieNode(curChar)
            curNode.nodeRecord[curChar] = newTrieNode
            curNode = newTrieNode
        curNode.end = True

    def search(self, word: str) -> bool:
        curNode = self.dummy
        for curChar in word:
            if curChar not in curNode.nodeRecord:
                return False
            curNode = curNode.nodeRecord[curChar]
        return curNode.end

    def startsWith(self, prefix: str) -> bool:
        curNode = self.dummy
        for curChar in prefix:
            if curChar not in curNode.nodeRecord:
                return False
            curNode = curNode.nodeRecord[curChar]
        return True
        
        