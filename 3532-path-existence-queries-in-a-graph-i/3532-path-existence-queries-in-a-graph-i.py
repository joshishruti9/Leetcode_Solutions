class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        res = []
        group = [0 for i in range(len(nums))]
        group_num = 0

        for i in range(1, len(nums)):
            if abs(nums[i] - nums[i-1]) <= maxDiff:
                group[i] = group[i-1]
            else:
                group_num += 1
                group[i] = group_num

        
        for qi, qj in queries:
            if group[qi] == group[qj]:
                res.append(True)
            else:
                res.append(False)
        
        return res