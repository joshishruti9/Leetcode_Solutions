class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_index_map = {}

        for index, num in enumerate(nums):
            if target - num in nums_index_map:
                return [index, nums_index_map[target-num]]
            
            nums_index_map[num] = index
        