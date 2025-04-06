# Last updated: 4/6/2025, 2:40:24 PM
class Solution:

    def find(self, x, root):
        if root[x] == x:
            return x
        return self.find(root[x], root)

    def union(self, x, y, rank, root):

        rx = self.find(x, root)
        ry = self.find(y, root)

        if rx == ry:
            return False
        
        if rank[rx] > rank[ry]:
            root[ry] = rx
        elif rank[rx] < rank[ry]:
            root[rx] = ry
        else:
            rank[rx] += 1
            root[ry] = rx

        return True

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        n = len(edges)
        root = [i for i in range(n+1)]
        rank = [1 for i in range(n+1)]
        output = []

        for x,y in edges:
            if not self.union(x, y, rank, root):
                return [x,y]