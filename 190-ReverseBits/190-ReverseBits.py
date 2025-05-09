# Last updated: 5/8/2025, 6:20:58 PM
class Solution:

    def reverseBits(self, n: int) -> int:
        bit_n = bin(n)
        n = 32 - len(bit_n[2:])

        rev_n = bit_n[2:][::-1]

        str_rev_n = "".join(rev_n)
        num =  int(str_rev_n,2)
        return num << n