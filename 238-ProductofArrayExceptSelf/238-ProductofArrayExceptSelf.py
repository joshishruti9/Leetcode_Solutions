class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        ltor = []
        rtol = []
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