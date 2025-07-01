# Last updated: 6/30/2025, 5:42:58 PM
class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        
        i = 0
        j = 1
        count = 0

        for i in range(len(nums)):
            curr_gcd = nums[i]
            for j in range(i, len(nums)):
                curr_gcd = gcd(curr_gcd, nums[j])
                if curr_gcd == k:
                    count += 1
                if curr_gcd < k:
                    break
        
        return count