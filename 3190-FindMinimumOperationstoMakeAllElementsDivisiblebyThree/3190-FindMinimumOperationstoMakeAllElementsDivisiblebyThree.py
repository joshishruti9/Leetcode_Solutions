# Last updated: 5/24/2025, 8:28:13 PM
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:

        count = 0

        for num in nums:
            if num % 3 == 0:
                continue
            else:
                count += 1

        return count
        