# Last updated: 7/9/2025, 5:05:33 PM
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:

        stack = []
        i = 0
        j = 0

        while j < len(pushed) and i < len(popped):
            if stack and popped[i] == stack[-1]:
                stack.pop()
                i += 1
            else:
                stack.append(pushed[j])
                j += 1

        while stack and i < len(popped):
            if popped[i] == stack[-1]:
                stack.pop()
                i += 1
            else:
                break

        return len(stack) == 0