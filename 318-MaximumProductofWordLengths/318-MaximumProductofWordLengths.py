# Last updated: 8/5/2025, 5:46:35 PM
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        max_len = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if not set(words[i]) & set(words[j]):
                    prod_len = len(words[i]) * len(words[j])
                    max_len = max(max_len, prod_len)

        return max_len
        