# Last updated: 5/8/2025, 3:37:13 PM
class Solution:
    def reverseBits(self, n: int) -> int:
        bit_n = bin(n)
        n = 32 - len(bit_n[2:])
        #print("bit_n ",bit_n[2:],"len",n)

        rev_n = bit_n[2:][::-1]
        if n > 0:
            while n > 0:
                rev_n += '0'
                n -= 1

        #print("rev_n", len(rev_n))

        str_rev_n = "".join(rev_n)
        #print("rev_n", str_rev_n)
        num =  int(str_rev_n,2)
        #print("num, ",num)
        return num