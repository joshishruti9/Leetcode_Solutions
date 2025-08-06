# Last updated: 8/6/2025, 2:53:22 PM
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        max_len = 0
    
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if not (set(words[i])).intersection(set(words[j])):
                    prod_len = len(words[i]) * len(words[j])
                    max_len = max(max_len, prod_len)

        return max_len