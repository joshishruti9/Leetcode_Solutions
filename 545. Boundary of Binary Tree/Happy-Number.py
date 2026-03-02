1class Solution:
2    def isHappy(self, n: int) -> bool:
3
4        if n == 1 or n == 7:
5            return True
6        
7        if n <= 9 and n >= 0:
8            return False
9        
10        total = 0
11        while n > 0:
12            total += ((n % 10) ** 2)
13            n = n // 10
14
15        return self.isHappy(total)
16
17        