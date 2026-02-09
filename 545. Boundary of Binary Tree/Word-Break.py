1class Solution:
2    def dp(self, s, wordset):
3        if s in self.memo:
4            return self.memo[s]
5        self.memo[s] = False 
6        for i in range(1, len(s) + 1):
7            if s[:i] in wordset and self.dp(s[i:], wordset):
8                self.memo[s] = True
9                break   
10        return self.memo[s]
11
12    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
13        wordSet = set(wordDict)
14        self.memo = {}
15        self.memo[""] = True
16        return self.dp(s, wordSet)
17        