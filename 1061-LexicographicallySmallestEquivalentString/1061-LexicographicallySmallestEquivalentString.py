# Last updated: 8/18/2025, 1:26:46 PM
class Solution:
    def find(self, root, x):
        if root[x] == x:
            return root[x]
        return self.find(root, root[x])

    def union_find(self, root, x, y):

        root_x = self.find(root, x)
        root_y = self.find(root, y)

        if root_x == root_y:
            return
        
        if root_x < root_y:
            root[root_y] = root_x
        else:
            root[root_x] = root_y

    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:

        root = {}
        res = []

        for letter1,letter2 in zip(s1,s2):
            root[letter1] = letter1
            root[letter2] = letter2

        for letter1, letter2 in zip(s1, s2):
            self.union_find(root, letter1, letter2) 
        
        for letter in baseStr:
            if letter in root:
                res.append(self.find(root, letter))
            else:
                res.append(letter)
        
        return "".join(res)