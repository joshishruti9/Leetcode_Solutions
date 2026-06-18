class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        ans = [0 for i in range(n)]

        ans[n-1] = 1

        for i in range(n-2, -1, -1):
            max_count = 1
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    max_count = max(max_count, ans[j]+1)

            ans[i] = max_count
        
        return max(ans)

        