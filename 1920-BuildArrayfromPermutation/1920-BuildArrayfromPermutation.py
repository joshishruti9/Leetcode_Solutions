# Last updated: 5/24/2025, 7:22:55 PM
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        res = []

        for i in range(len(nums)):
            res.append(nums[nums[i]])
        
        return res