# Last updated: 4/12/2025, 6:30:06 PM
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        total = sum(nums[0:k])
        i = 0
        j = k-1
        max_avg = (total/k)

        while j < len(nums)-1:
            total -= nums[i]
            i += 1
            j += 1
            total += nums[j]
            max_avg = max(max_avg, (total/k))
        #max_avg = max(max_avg, (total/k))   
        return max_avg