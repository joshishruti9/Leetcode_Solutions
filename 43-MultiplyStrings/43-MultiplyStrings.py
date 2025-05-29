# Last updated: 5/29/2025, 4:56:58 PM
class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        n1 = len(num1) - 1
        n2 = len(num2) - 1
        ans = 0
        digit = 0

        for i in range(n1,-1,-1):
            carry = 0
            count = 0
            mul = 0
            for j in range(n2, -1, -1):
                num = int(num2[j]) * int(num1[i]) % 10
                mul += ((10 ** count) * (num + carry))
                carry = int(num2[j]) * int(num1[i]) // 10
                count += 1
            
            if carry > 0:
                mul = carry * (10 ** count) + mul
            
            mul = mul * (10 ** digit)
            ans += mul
            digit += 1

        return str(ans)