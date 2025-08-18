# Last updated: 8/18/2025, 12:41:15 PM
class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0
        max_count = 0

        for char in s:
            if char == '(':
                count += 1
                max_count = max(max_count, count)
            elif char == ')':
                count -= 1
            else:
                continue
        
        return max_count