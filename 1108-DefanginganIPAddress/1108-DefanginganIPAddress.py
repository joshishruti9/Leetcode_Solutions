# Last updated: 5/25/2025, 7:48:33 PM
class Solution:
    def defangIPaddr(self, address: str) -> str:
        res = []

        for char in address:
            if char == '.':
                res.append('[')
                res.append('.')
                res.append(']')
            else:
                res.append(char)
        
        return "".join(res)
        