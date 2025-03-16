class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        vowels_arr = []
        p1 = 0
        p2 = len(s) - 1
        res = list(s)

        while p1 < p2:
            if res[p1] in vowels and res[p2] in vowels:
                res[p1], res[p2] = res[p2], res[p1]
                p1 += 1
                p2 -= 1
            elif res[p1] in vowels:
                p2 -= 1
            else:
                p1 += 1

        return "".join(res)