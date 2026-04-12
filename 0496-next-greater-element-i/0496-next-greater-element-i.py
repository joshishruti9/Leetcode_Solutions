class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        res = []
        stack = []
        hmap = {}

        for i in range(len(nums2)):
            while stack and nums2[stack[-1]] < nums2[i]:
                item = stack.pop()
                hmap[nums2[item]] = nums2[i] 
            else:
                stack.append(i)

        
        for num in nums1:
            if num in hmap:
                res.append(hmap[num])
            else:
                res.append(-1)

        return res
        