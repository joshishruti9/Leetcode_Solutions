class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n

        so_far_left_prd = 1
        ans[0] = 1
        for i in range(1, n):
            so_far_left_prd *= nums[i-1]
            ans[i] = so_far_left_prd
            
        so_far_right_prd = 1
        for i in range(n-2, -1, -1):
            so_far_right_prd *= nums[i+1]
            ans[i] *= so_far_right_prd  

        return ans