# Last updated: 4/13/2025, 3:29:34 PM
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        start = 0
        end = 0
        res = []

        if len(nums) == 0:
            return []
        
        while end < len(nums)-1:
            if nums[end] + 1 == nums[end+1]:
                end += 1
            else:
                if start != end:
                    res.append(str(nums[start]) + "->" + str(nums[end]))
                    end += 1
                    start = end
                else:
                    res.append(str(nums[start]))
                    start += 1
                    end += 1
        if start != end:
            res.append(str(nums[start]) + "->" + str(nums[end]))
        else:
            res.append(str(nums[start]))
                    
        return res