# Last updated: 4/29/2025, 4:20:20 PM
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 1

        i = 1
        j = 1


        while i < len(nums):
            if nums[i-1] == nums[i]:
                count += 1
            else:
                count = 1

            if count <= 2:
                nums[j] = nums[i]
                j += 1
            
            i += 1

        return j

        