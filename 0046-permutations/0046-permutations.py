class Solution:
    def traverse(self, curr_res, nums, visited):

        if len(nums) == len(curr_res):
            self.res.append(curr_res[:])
            return

        for i in range(len(nums)):
            if nums[i] not in visited:
                visited.add(nums[i])
                curr_res.append(nums[i])
                self.traverse(curr_res, nums, visited)
                curr_res.pop()
                visited.remove(nums[i])
        

    def permute(self, nums: List[int]) -> List[List[int]]:

        self.res = []

        self.traverse([], nums, set()) 
        
        return self.res