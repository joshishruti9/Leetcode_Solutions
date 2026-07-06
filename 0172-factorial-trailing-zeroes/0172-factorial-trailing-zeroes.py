class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0 

        count = n // 5
        count += n // 25
        count += n // 125
        count += n // 625
        count += n // 3125

        return count
        