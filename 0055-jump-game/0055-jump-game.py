class Solution:
    def dp(self, i, nums):
        if i in self.memo:
            return self.memo[i]
        
        max_index = nums[i] + i

        if self.last_true <= max_index:
            self.last_true = i
            self.memo[i] = True
            return True


        self.memo[i] = False  
        for j in range(1, nums[i]+1):
            flag = self.memo[i] or self.dp(i+j, nums)

            if flag:
                self.memo[i] = True
                self.last_true = i
                break
        
        
        return self.memo[i]

    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        self.memo = {}

        self.memo[n-1] = True
        self.last_true = n-1

        self.dp(0, nums)

        return self.memo[0]