class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        hmap = {}

        i = 0
        j = 0
        max_len = 0

        while j < len(s):
            if s[j] in hmap:
                max_len = max(max_len, j-i)
                next_index = hmap[s[j]]
                
                while i <= next_index:
                    hmap[s[i]] -= 1
                    if hmap[s[i]] == 0:
                        hmap.pop(s[i])
                    i += 1
                
            hmap[s[j]] = j
            j += 1

        max_len = max(max_len, j-i)
        return max_len

        