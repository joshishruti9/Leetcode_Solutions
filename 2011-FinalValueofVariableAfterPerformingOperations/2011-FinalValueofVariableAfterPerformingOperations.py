# Last updated: 5/24/2025, 8:16:20 PM
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        num = 0

        for operation in operations:
            if '++' in operation:
                num += 1
            else:
                num -= 1
        return num
        