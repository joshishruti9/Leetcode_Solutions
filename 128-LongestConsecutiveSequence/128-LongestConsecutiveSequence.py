# Last updated: 8/4/2025, 4:48:14 PM
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numset = set(nums)
        count = 0
        max_count = 0

        for num in numset:
            if num-1 not in numset:
                count = 1
                curr_num = num + 1
                while curr_num in numset:
                    count += 1
                    curr_num += 1
                max_count = max(count, max_count)
        
        return max_count

