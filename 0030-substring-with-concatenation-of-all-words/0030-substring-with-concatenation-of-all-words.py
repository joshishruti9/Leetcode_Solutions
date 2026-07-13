from collections import Counter, defaultdict

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:

        res = []

        if not s or not words:
            return res

        word_len = len(words[0])
        total_words = len(words)

        need = Counter(words)

        # Try every possible starting offset
        for offset in range(word_len):

            left = offset
            right = offset

            window = defaultdict(int)
            count = 0   # number of valid words in current window

            while right + word_len <= len(s):

                # Get next word
                word = s[right:right + word_len]
                right += word_len

                # If word is not in dictionary, reset window
                if word not in need:
                    window.clear()
                    count = 0
                    left = right
                    continue

                # Add word to window
                window[word] += 1
                count += 1

                # If this word appears too many times, remove from left
                while window[word] > need[word]:

                    left_word = s[left:left + word_len]

                    window[left_word] -= 1
                    count -= 1

                    left += word_len


                # All words matched
                if count == total_words:
                    res.append(left)

                    # Slide once to look for next answer
                    left_word = s[left:left + word_len]

                    window[left_word] -= 1
                    count -= 1

                    left += word_len

        return res