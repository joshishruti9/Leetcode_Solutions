class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        nums_index_map = {}

        for i, num in enumerate(nums):
            if num in nums_index_map:
                j = nums_index_map[num]
                if abs(i-j) <= k:
                    return True
            
            nums_index_map[num] = i
        
        return False
        