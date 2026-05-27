class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        path_str = path.split("/")
        
        for element in path_str:
            print(element)

            if element == '/' or element == '.' or element == "":
                    continue
            elif element == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(element)
        
        return "/" + "/".join(stack)
        