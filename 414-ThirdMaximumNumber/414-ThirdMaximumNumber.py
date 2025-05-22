# Last updated: 5/22/2025, 2:44:36 PM
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        max1 = max2 = max3 = float('-inf')

        if len(nums) < 3:
            return max(nums)

        for i in range(len(nums)):
            if nums[i] < max3:
                continue
            elif nums[i] == max3:
                continue
            else:
                if nums[i] < max2:
                    max3 = nums[i]
                elif nums[i] == max2:
                    continue
                else:
                    if nums[i] < max1:
                        max3 = max2
                        max2 = nums[i]
                    elif nums[i] == max1:
                        continue
                    else:
                        max3 = max2
                        max2 = max1
                        max1 = nums[i]

        return max3 if max3 != float('-inf') else max1