# Last updated: 7/2/2025, 4:58:22 PM
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:

        min_heap = []
        res = []
        total = 0

        l1 = len(nums1)
        l2 = len(nums2)

        occured = set()

        total = nums1[0] + nums2[0]
        heappush(min_heap,(total, 0, 0))
        
        while k > 0:
            total, i, j = heappop(min_heap)
            res.append([nums1[i],nums2[j]]) 

            if i+1 < l1 and (i+1, j) not in occured:
                total = nums1[i+1] + nums2[j]
                heappush(min_heap,(total,i+1,j))
                occured.add((i+1,j))
            
            if j+1 < l2 and (i, j+1) not in occured:
                total = nums1[i] + nums2[j+1]
                heappush(min_heap,(total,i,j+1))
                occured.add((i,j+1))
            
            k -= 1
        
        return res