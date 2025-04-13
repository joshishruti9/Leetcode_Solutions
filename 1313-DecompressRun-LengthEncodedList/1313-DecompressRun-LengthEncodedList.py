# Last updated: 4/13/2025, 4:33:25 PM
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        i = 0
        res = []
        while i < len(nums)-1:
            freq = nums[i]
            val = nums[i+1]

            for j in range(freq):
                res.append(val)
            
            i += 2

        return res