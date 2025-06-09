# Last updated: 6/8/2025, 5:26:52 PM
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        bracket_map = {")":"(","]":"[","}":"{"}

        for char in s:
            if char not in bracket_map:
                stack.append(char)
            else:
                if stack and bracket_map[char] == stack[-1]:
                    stack.pop()
                else:
                    return False

        return not stack