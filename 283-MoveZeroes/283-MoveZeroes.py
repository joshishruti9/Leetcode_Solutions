class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = 0
        i = 0
        while i < len(nums):
            if nums[i] != 0:
                nums[k] = nums[i]
                k += 1
            i += 1
        
        while k < len(nums):
            nums[k] = 0
            k += 1