class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hmap = {}
        max_len = 0
        i = j = 0

        while j < len(s):
            if s[j] not in hmap:
                hmap[s[j]] = hmap.get(s[j],0) + 1
                j += 1
            else:
                max_len = max(max_len, (j-i))
                if s[i] in hmap:
                    hmap[s[i]] -= 1
                    if hmap[s[i]] == 0:
                        hmap.pop(s[i])
                    
                i += 1 

        max_len = max(max_len, (j-i))   
        return max_len