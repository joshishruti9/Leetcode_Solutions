# Last updated: 3/29/2025, 4:26:37 PM
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        next_great_map = dict()

        for num in nums2:
            while stack and stack[-1] < num:
                last_item = stack.pop()
                next_great_map[last_item] = num
            else:
                stack.append(num)

        while stack:
            last_item = stack.pop()
            next_great_map[last_item] = -1

        result = []
        for num in nums1:
            result.append(next_great_map[num])
        
        return result