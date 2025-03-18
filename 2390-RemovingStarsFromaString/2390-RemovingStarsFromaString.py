class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        i = 0
        while i < len(s):
            if s[i] == "*":
                if stack:
                    stack.pop()
                else:
                    return ""
            else:
                stack.append(s[i])
            i += 1
        return "".join(stack)
        