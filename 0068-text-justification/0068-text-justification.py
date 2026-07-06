class Solution:
    def justify(self, maxWidth, curr_len, output):

        remain_space = maxWidth - curr_len

        if len(output) == 1:
            self.res.append(output[0] + " " * remain_space)
            return

        gaps = len(output) - 1
        space_bet_each_word = remain_space // gaps
        extra_space = remain_space % gaps
    
        temp = []
        for i in range(gaps):
            temp.append(output[i] + " " * space_bet_each_word)
            if i < extra_space:
                temp.append(" ")
        
        temp.append(output[-1])
        self.res.append("".join(temp))

    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

        self.res = []
        output = []
        curr_len = 0

        for word in words:
    
            if (len(word) + curr_len + len(output)) <= maxWidth:
                output.append(word)
                curr_len += len(word)
            else:
                self.justify(maxWidth, curr_len, output)
                output = [word]
                curr_len = len(word)
        
        last_line = " ".join(output)
        last_line += " " * (maxWidth - len(last_line))
        self.res.append(last_line)

        return self.res