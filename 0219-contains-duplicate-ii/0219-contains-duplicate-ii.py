class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        hmap = {}

        for i, num in enumerate(nums):
            if num in hmap:
                last_pos = hmap[num]
                if k >= abs(i-last_pos):
                    return True
            hmap[num] = i

        return False
        