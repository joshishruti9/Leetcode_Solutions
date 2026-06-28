class Solution:
    def traverse(self, word1, word2, i, j):

        if (i ,j) in self.memo:
            return self.memo[(i, j)]

        if i == len(word1) or j == len(word2):
            if i == len(word1):
                curr_res = (len(word2) - j)
            elif j == len(word2):
                curr_res = (len(word1) - i)

            self.memo[(i, j)] = curr_res
            return self.memo[(i, j)]
        
        ans1 = ans2 = ans3 = float("inf")

        if word1[i] == word2[j]:
            result = self.traverse(word1 , word2, i+1, j+1)
            self.memo[(i, j)] = result
        else:
            ans1 = self.traverse(word1, word2, i+1, j)
            ans2 = self.traverse(word1, word2, i, j+1)
            self.memo[(i, j)] = 1 + min(ans1, ans2)
        
        return self.memo[(i, j)]

    def minDistance(self, word1: str, word2: str) -> int:

        self.memo = {}

        self.traverse(word1, word2, 0, 0)

        return self.memo[(0,0)]


        