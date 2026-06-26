class Solution:
    def __init__(self):
        self.trie = {}

    def traverse(self, board, i, j, m, n, visited, node, res):

        letter = board[i][j]
        
        if letter not in node:
            return

        node = node[letter]

        if "end" in node:
            res.append(node["end"])
            del node["end"]

        dirs = [(1,0), (0,1), (0,-1), (-1,0)]
        direction = 0
                
        visited.add((i, j))
        for di, dj in dirs:
            if 0 <= i+di < m and 0 <= j+dj < n and (i+di, j+dj) not in visited:
                if board[i+di][j+dj] in node:
                    self.traverse(board, i+di, j+dj, m, n, visited, node, res)
        
        visited.remove((i, j))
    
    def create_trie(self, words):
        for word in words:
            node = self.trie
            for letter in word:
                if letter not in node:
                    node[letter] = {}
                node = node[letter]

            node["end"] = word
        
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        res = []

        self.create_trie(words)

        m = len(board)
        n = len(board[0])
    
        for i in range(m):
            for j in range(n):
                self.traverse(board, i, j, m, n, set(), self.trie, res)
                   
                            
        return res