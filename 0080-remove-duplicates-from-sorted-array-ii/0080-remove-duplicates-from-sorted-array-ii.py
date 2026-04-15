class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        count = 0
        k = 1

        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]:
                count += 1
            else:
                count = 0
            
            if count <= 1:
                nums[k] = nums[i]
                k += 1

        return k
        