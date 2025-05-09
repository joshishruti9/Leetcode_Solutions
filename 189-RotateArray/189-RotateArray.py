# Last updated: 5/8/2025, 6:50:24 PM
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n


        #one way
        '''st = []
        for i in range(n-1,n-1-k,-1):
            st.append(nums[i])
            
        for i in range(n-1-k,-1,-1):
            nums[i+k] = nums[i]
        
        for i in range(0,k):
            nums[i] = st.pop()'''
        

        #second way
        nums[:] = nums[n-k:] + nums[:n-k]
