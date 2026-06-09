class Solution:

    def hammingWeight(self, n: int) -> int:
        one_count = 0
        while n > 0:
            num = n & 1
            if num == 1:
                one_count += 1
            
            n = n >> 1
        
        return one_count