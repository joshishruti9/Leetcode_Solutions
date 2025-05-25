# Last updated: 5/24/2025, 8:23:26 PM
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:

        i = 0
        j = n
        res = []

        while j < len(nums) and i < j:
            res.append(nums[i])
            res.append(nums[j])

            i += 1
            j += 1
        
        return res