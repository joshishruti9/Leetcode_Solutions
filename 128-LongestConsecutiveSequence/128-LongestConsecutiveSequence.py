# Last updated: 8/4/2025, 4:32:36 PM
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numsset = set(nums)
        max_count = 0
        count = 0

        for num in numsset:
            if num - 1 not in numsset:
                count = 1
                curr_num = num
                while curr_num + 1 in numsset:
                    count += 1
                    curr_num += 1
                max_count = max(max_count, count)
        
        return max_count      