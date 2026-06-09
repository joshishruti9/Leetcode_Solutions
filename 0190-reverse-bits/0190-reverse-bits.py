class Solution:
    def reverseBits(self, n: int) -> int:

        binary_num = bin(n)
        remain_bit = 32 - len(binary_num) + 2
        reversed_binary_num = list(binary_num[2:][::-1])
        
        for i in range(remain_bit):
            reversed_binary_num.append('0')

        num = int("".join(reversed_binary_num), 2)
        return num
        