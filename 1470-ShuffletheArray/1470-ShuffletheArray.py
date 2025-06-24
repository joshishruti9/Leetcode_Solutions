# Last updated: 6/23/2025, 11:05:08 PM
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:

        i = 0
        j = n

        res = []

        while j < len(nums):
            res.append(nums[i])
            res.append(nums[j])

            i += 1
            j += 1

        return res