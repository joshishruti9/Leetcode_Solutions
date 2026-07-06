class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0 
        mul = 5

        while mul <= n:
            count += n // mul
            mul = mul * 5

        return count
        