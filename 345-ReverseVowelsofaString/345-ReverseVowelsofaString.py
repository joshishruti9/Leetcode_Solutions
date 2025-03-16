class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        vowels_arr = []

        for i in range(len(s)):
            if s[i] in vowels:
                vowels_arr.append(s[i])

        j = len(vowels_arr)-1
        res = []
        for i in range(len(s)): 
            if s[i] in vowels:
                res.append(vowels_arr[j]) 
                j -= 1
            else:
                res.append(s[i])
        return "".join(res)