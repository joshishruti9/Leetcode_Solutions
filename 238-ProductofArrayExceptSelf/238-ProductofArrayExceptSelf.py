# Last updated: 4/17/2025, 3:56:37 PM
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        ltor = []
        rtol = [0 for i in range(len(nums))]
        n = len(nums)

        product = 1
    
        for i in range(n):
            product *= nums[i] 
            ltor.append(product)
    
        product = 1
        for i in range(n-1,-1,-1):
            product *= nums[i]
            rtol.append(product)
        
        rtol = rtol[::-1]

        res.append(rtol[1])
        for i in range(1,n-1):
            res.append(ltor[i-1] * rtol[i+1])
        res.append(ltor[n-2])

        return res