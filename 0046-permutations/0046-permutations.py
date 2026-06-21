class Solution:
    def traverse(self, nums, curr_res, visited):
        if len(curr_res) == len(nums):
            self.output.append(curr_res[:])
        
        for i in range(len(nums)):
            if nums[i] not in visited:
                curr_res.append(nums[i])
                visited.add(nums[i])
                self.traverse(nums, curr_res, visited)
                visited.remove(nums[i])
                curr_res.pop()
        
        return

    def permute(self, nums: List[int]) -> List[List[int]]:

        self.output = []
        self.traverse(nums, [], set())
        return self.output
        