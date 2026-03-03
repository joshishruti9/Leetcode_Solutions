1class Trie:
2
3    def __init__(self):
4        self.hmap = {'end':True}
5        
6
7    def insert(self, word: str) -> None:
8        curr = self.hmap
9        
10        for char in word:
11            if char in curr:
12                curr = curr[char]
13            else:
14                curr[char] = {'end':False}
15                curr = curr[char]
16        curr['end'] = True
17        
18    def search(self, word: str) -> bool:
19        
20        curr = self.hmap
21        
22        for char in word:
23            if char in curr:
24                curr = curr[char]
25            else:
26                return False
27        
28        return curr['end']
29
30    def startsWith(self, prefix: str) -> bool:
31        curr = self.hmap
32        
33        for char in prefix:
34            if char in curr:
35                curr = curr[char]
36            else:
37                return False
38        
39        return True
40        
41
42
43# Your Trie object will be instantiated and called as such:
44# obj = Trie()
45# obj.insert(word)
46# param_2 = obj.search(word)
47# param_3 = obj.startsWith(prefix)