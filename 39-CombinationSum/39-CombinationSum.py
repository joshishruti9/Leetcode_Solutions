# Last updated: 5/6/2025, 10:31:21 PM
class Solution:
    def traverse(self, nums, target, curr_res, curr_index):

        if target == 0:
            self.res.append(curr_res[:])
        if target < 0:
            return


        for i in range(curr_index, len(nums)):
            curr_res.append(nums[i])
            self.traverse(nums, target-nums[i], curr_res, i)
            curr_res.remove(nums[i])

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = []

        self.traverse(candidates, target, [], 0)

        return self.res