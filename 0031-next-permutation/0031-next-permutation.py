class Solution:

    def reverse(self, nums, j):
        nums[j:] = nums[j:][::-1]

    def swap(self, nums, j):
        curr_min_index = j + 1
        for k in range(j + 1, len(nums)):
            if nums[k] <= nums[curr_min_index] and nums[k] > nums[j]:
                curr_min_index = k
        nums[j], nums[curr_min_index] = nums[curr_min_index], nums[j]
    
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        n = len(nums)

        if n == 1:
            return
        
        for i in range(n - 1, 0, -1):
            if nums[i-1] < nums[i]:
                self.swap(nums, i - 1)
                self.reverse(nums, i)
                return
        
        nums[:] = nums[::-1]
        
