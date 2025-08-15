# Last updated: 8/15/2025, 2:56:23 PM
from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        stack = []
        total = 0

        i = 0
        curr_high = height[i]

        while i < len(height):
            if height[i] < curr_high:
                stack.append(height[i])
            else:
                while stack:
                    total += (curr_high - stack.pop())
                curr_high = height[i]
            i += 1

        # Handle case where water is trapped using the right boundary
        if stack:
            right_high = stack.pop()
            while stack:
                h = stack.pop()
                total += max(0, right_high - h)
                right_high = max(right_high, h)

        return total