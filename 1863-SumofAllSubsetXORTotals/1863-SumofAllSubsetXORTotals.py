# Last updated: 5/24/2025, 8:10:01 PM
class Solution:
    def traverse(self, nums, curr_xor, index):
        if index == len(nums):
            return 
        
        for i in range(index, len(nums)):
            self.res += curr_xor ^ nums[i]
            self.traverse(nums, curr_xor ^ nums[i], i+1)
    
    def subsetXORSum(self, nums: List[int]) -> int:
        self.res = 0
        self.traverse(nums, 0, 0)
        
        return self.res