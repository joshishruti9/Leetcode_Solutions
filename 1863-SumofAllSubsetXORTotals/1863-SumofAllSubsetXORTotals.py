# Last updated: 5/24/2025, 8:11:00 PM
class Solution:
    def traverse(self, nums, curr_xor, index):
        if index == len(nums):
            return 
        for i in range(index, len(nums)):
            new_xor = curr_xor ^ nums[i]
            self.res += new_xor
            self.traverse(nums, new_xor, i+1)
    
    def subsetXORSum(self, nums: List[int]) -> int:
        self.res = 0
        self.traverse(nums, 0, 0)
        return self.res