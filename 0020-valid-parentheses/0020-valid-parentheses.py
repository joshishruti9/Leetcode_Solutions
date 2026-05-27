class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        brackets = {'}':'{', ')':'(', ']':'['}

        for char in s:
            if char not in brackets:
                stack.append(char)
            else:
                if stack and stack[-1] == brackets[char]:
                    stack.pop()
                else:
                   return False 
        
        return not stack