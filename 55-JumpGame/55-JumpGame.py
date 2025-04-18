# Last updated: 4/17/2025, 10:52:47 PM
class Solution:
    def dp(self, index, nums):

        if index not in self.memo:
            self.memo[index] = False

            k = index + nums[index]
            if k >= self.last_true:
                self.memo[index] = True
                self.last_true = index
                return True

            for j in range(1, nums[index]+1):
                if index + j < len(nums):
                    self.memo[index] = self.memo[index] or self.dp(index+j, nums)
                    if self.memo[index]:
                        self.last_true = index
                        break

        return self.memo[index]

    def canJump(self, nums: List[int]) -> bool:
        self.memo = {}
        n = len(nums)

        self.last_true = n-1
        self.memo[n-1] = True

        self.dp(0, nums)

        return self.memo[0]    