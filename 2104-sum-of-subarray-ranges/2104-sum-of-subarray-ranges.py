class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:

        diff = 0

        for i in range(len(nums)):
            max_num = nums[i]
            min_num = nums[i]

            for j in range(i+1, len(nums)):

                min_num = min(min_num, nums[j])
                max_num = max(max_num, nums[j])

                diff += max_num - min_num
        
        return diff
        