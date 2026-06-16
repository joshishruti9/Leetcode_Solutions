class Solution:
    def dp(self, s, wordset, start, end):
        if s[start:end] in self.memo:
            return self.memo[s[start: end]]
        
        i = start + 1
        while i <= end:

            if s[start:i] in wordset:
                self.memo[s[start:i]] = True
                if self.dp(s, wordset, i, end):
                    self.memo[s[start:end]] = True
                    return self.memo[s[start:end]]
            
            i += 1

        self.memo[s[start:end]] = False
        return self.memo[s[start:end]]


    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        self.memo = {}
        self.memo[""] = True

        return self.dp(s, set(wordDict), 0, len(s))
        