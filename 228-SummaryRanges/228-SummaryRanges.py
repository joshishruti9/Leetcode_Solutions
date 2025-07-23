# Last updated: 7/23/2025, 11:48:34 AM
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        start = 0
        end = 0
        res = []

        if len(nums) == 0:
            return res

        while end < len(nums)-1:

            if nums[end] == nums[end+1]-1:
                end += 1
            else:
                if start == end:
                    res.append(str(nums[start]))
                    start += 1
                    end += 1
                else:
                    res.append(str(nums[start]) + "->" + str(nums[end]))
                    end += 1
                    start = end

        if start == end:
            res.append(str(nums[start]))
        else:
            res.append(str(nums[start]) + "->" + str(nums[end]))

        return res