class Solution:
    def backtrack(self, curr_sum, target, candidates, curr_res, curr_index):
        if curr_sum == target:
            self.output.append(curr_res[:])
            return
        
        if curr_sum > target:
            return

        for i in range(curr_index, len(candidates)):
            curr_res.append(candidates[i])
            self.backtrack(curr_sum + candidates[i], target, candidates, curr_res, i)
            curr_res.pop()

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        self.output = []
        self.backtrack(0, target, candidates, [], 0)
        return self.output
        