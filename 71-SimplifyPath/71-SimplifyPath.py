class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        paths = path.split("/")

        for directory in paths:
            if directory == "..":
                if stack:
                    stack.pop()
            elif directory == "." or directory == "/" or directory == "":
                continue
            else:
                stack.append(directory)
        

        return '/' + "/".join(stack)
        
        