class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        bit_count = 0

        while n:
            last_bit = n & 1
            res = (res << 1) + last_bit
            n = n >> 1
            bit_count += 1

        res = res << (32-bit_count)

        return res
