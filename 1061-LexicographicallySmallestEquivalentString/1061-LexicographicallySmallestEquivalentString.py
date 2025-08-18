# Last updated: 8/18/2025, 1:25:44 PM
class Solution:
    def find(self, root, x):
        if root[x] == x:
            return root[x]
        return self.find(root, root[x])

    def union_find(self, root, rank, x, y):

        root_x = self.find(root, x)
        root_y = self.find(root, y)

        if root_x == root_y:
            return
        
        if root_x < root_y:
            root[root_y] = root_x
        else:
            root[root_x] = root_y


        '''if rank[root_x] > rank[root_y]:
            root_x < root_y
            root[root_y] = root_x
        elif rank[root_y] > rank[root_x]:
            root[root_x] = root_y
        else:
            if x <= y:
                root[root_y] = root_x
                rank[root_x] += 1
            else:
                root[root_x] = root_y
                rank[root_y] += 1 '''

    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:

        root = {}
        rank = {}
        res = []

        for letter1,letter2 in zip(s1,s2):
            root[letter1] = letter1
            root[letter2] = letter2
            rank[letter1] = 1
            rank[letter2] = 1

        for letter1, letter2 in zip(s1, s2):
            self.union_find(root, rank, letter1, letter2) 
        
        for letter in baseStr:
            if letter in root:
                res.append(self.find(root, letter))
            else:
                res.append(letter)
        
        return "".join(res)