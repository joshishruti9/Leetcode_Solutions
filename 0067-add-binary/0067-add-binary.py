class Solution:
    def addBinary(self, a: str, b: str) -> str:
        binary_a = int(a, 2)
        binary_b = int(b, 2)

        return str(bin((binary_a + binary_b)))[2:]      