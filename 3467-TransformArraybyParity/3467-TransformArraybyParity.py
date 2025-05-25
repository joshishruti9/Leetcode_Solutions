# Last updated: 5/24/2025, 8:19:42 PM
class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:

        even = 0
        odd = 0
        res = []

        for num in nums:
            if num % 2 == 0:
                even += 1
            else:
                odd += 1
        
        for i in range(even):
            res.append(0)
        
        for i in range(odd):
            res.append(1)

        return res
        