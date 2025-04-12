# Last updated: 4/12/2025, 4:51:24 PM
class Solution:
    def hammingWeight(self, n: int) -> int:

        binary_n = bin(n)
        count = 0

        for i in range(2,len(binary_n)):
            if binary_n[i] == "1":
                count += 1
        return count
        