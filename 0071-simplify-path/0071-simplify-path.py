class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        path_str = path.split("/")
        
        for element in path_str:
            if element == '' or element == '.':
                    continue
            elif element == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(element)
        
        return "/" + "/".join(stack)
        