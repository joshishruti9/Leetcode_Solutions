# Last updated: 6/23/2025, 10:46:03 PM
class Solution:
    def traverse(self, num, n, curr_res):
        if num > n or len(curr_res) == n:
            return
        
        i = num
        while i <= min(n, num + 9):
                             
            if i == 0: 
                i += 1
                continue
            curr_res.append(i)
            self.traverse(i*10, n, curr_res)
            i += 1
        

    def lexicalOrder(self, n: int) -> List[int]:
        
        i = 1

        res = []

        self.traverse(0, n, res)

        return res