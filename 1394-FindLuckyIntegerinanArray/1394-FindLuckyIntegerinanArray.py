# Last updated: 6/23/2025, 11:02:21 PM
class Solution:
    def findLucky(self, arr: List[int]) -> int:

        hmap = dict()
        ans = -1

        for num in arr:
            if num in hmap:
                hmap[num] += 1
            else:
                hmap[num] = 1
        
        for key, value in hmap.items():
            if key == value:
                ans = max(ans,key)

        return ans
        