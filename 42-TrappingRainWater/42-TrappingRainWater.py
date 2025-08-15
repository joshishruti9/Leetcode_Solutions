# Last updated: 8/15/2025, 3:12:42 PM
class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        total = 0

        i = 0
        while i< len(height) and height[i] <= 0:
            i += 1
        
        if i == len(height):
            return 0

        curr_high = height[i]

        while i < len(height):
            if height[i] <= curr_high:
                stack.append(height[i])
                i += 1
            else:
                min_val = min(curr_high, height[i])
                max_val = max(curr_high, height[i])
                while stack:
                    val = stack.pop()
                    total += (min_val - val)
                curr_high = height[i]
                stack.append(height[i])
                i += 1

        if stack:
            right_max = stack.pop()
            while stack:
                val = stack.pop()
                if val > right_max:
                    right_max = val
                else:
                    total += (right_max - val)

        return total