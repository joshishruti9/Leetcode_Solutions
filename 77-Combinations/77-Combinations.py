# Last updated: 4/8/2025, 2:10:28 PM
class Solution:
    def traverse(self, n, k, curr_num, curr_output):
        if len(curr_output) == k:
            self.output.append(curr_output)
            return

        for i in range(curr_num, n+1):
            new_output = curr_output[:]
            new_output.append(i)
            self.traverse(n, k, i+1, new_output)
            
        return
   
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.output = []

        self.traverse(n, k, 1, []) 

        return self.output