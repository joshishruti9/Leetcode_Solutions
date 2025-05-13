# Last updated: 5/13/2025, 1:31:25 PM
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ptr1 = 0
        ptr2 = 0
        visited = set()
        max_len = 0

        while ptr2 < len(s):
            if s[ptr2] in visited:
                max_len = max(max_len,(ptr2-ptr1))
                visited.remove(s[ptr1])
                ptr1 += 1
            else:
                visited.add(s[ptr2])
                ptr2 += 1
        max_len = max(max_len,(ptr2-ptr1))

        return max_len