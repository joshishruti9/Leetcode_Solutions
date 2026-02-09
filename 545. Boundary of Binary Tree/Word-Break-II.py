1class Solution:
2    def dp(self, s, wordset, output):
3        if s == "":
4            res_str = " ".join(output)
5            self.res.append(res_str)
6            return
7
8
9        self.memo[s] = False
10        for i in range(1, len(s)+1):
11            if s[:i] in wordset:
12                output.append(s[:i])
13                self.dp(s[i:], wordset, output)
14                output.pop()
15        
16
17    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
18
19        self.memo = {}
20        self.memo[""] = True
21        self.res = []
22
23        self.dp(s, set(wordDict), []) 
24
25        return self.res
26        