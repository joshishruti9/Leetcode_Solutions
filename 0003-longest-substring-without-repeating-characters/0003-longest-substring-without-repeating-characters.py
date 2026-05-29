class Solution:
    # Take 2 pointers start and end and a dictionary. 
    def lengthOfLongestSubstring(self, s: str) -> int:
        hmap = {}

        start = 0
        end = 0
        max_len = 0

        while end < len(s):
            if s[end] in hmap:
                max_len = max(max_len, end-start)
                last_index = hmap[s[end]]
                while start <= last_index:
                    if hmap[s[start]] <  last_index:
                        hmap.pop(s[start])

                    start += 1
            
            hmap[s[end]] = end
            end += 1

        max_len = max(max_len, end-start)
        return max_len