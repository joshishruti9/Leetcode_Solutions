class Solution:
    def traverse(self, n, k, curr_res, curr_index):
        if len(curr_res) == k:
            self.res.append(curr_res[:])
            return
        
        for i in range(curr_index, n+1):
            curr_res.append(i)
            self.traverse(n, k, curr_res, i+1)
            curr_res.pop()
        
        return


    def combine(self, n: int, k: int) -> List[List[int]]:
        self.res = []
        self.traverse(n, k, [], 1)

        return self.res

        