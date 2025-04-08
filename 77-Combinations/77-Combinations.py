# Last updated: 4/8/2025, 1:54:30 PM
class Solution:
    def traverse(self, n, k, curr_num, curr_output):
        if len(curr_output) == k:
            self.output.append(curr_output[:])
            return

        for i in range(curr_num, n+1):
            curr_output.append(i)
            self.traverse(n, k, i+1, curr_output)
            curr_output.pop()
        return
   

    def combine(self, n: int, k: int) -> List[List[int]]:
        self.output = []

        self.traverse(n, k, 1, []) 

        return self.output
        