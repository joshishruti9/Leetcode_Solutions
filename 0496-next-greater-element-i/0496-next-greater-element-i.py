class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        res = []
        num_dict = {}
        stack = []

        for i in range(len(nums2)):
            while stack and nums2[stack[-1]] < nums2[i]:
                index = stack.pop()
                num_dict[nums2[index]] = nums2[i]
            
            stack.append(i)
        

        for num in nums1:
            res.append(num_dict.get(num, -1))
        
        return res
        