# Last updated: 7/9/2025, 4:28:47 PM
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:

        letters = set(brokenLetters)
        count = 0
        i = 0
        n = len(text)
        flag = False

        while i < n:
            if text[i] in letters:
                while i < n and text[i] != " ":
                    flag = False
                    i += 1
            elif text[i] not in letters:
                if text[i] == " ":
                    if flag:
                        count += 1
                        flag = False
                    i += 1
                    continue
                else:
                    flag = True
                    i += 1   
        
        if flag:
            count += 1
        
        return count