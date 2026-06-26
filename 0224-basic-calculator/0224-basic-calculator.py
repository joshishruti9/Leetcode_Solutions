class Solution:
    def calculate(self, s: str) -> int:

        stack = []
        sign = 1
        res = 0
        num = 0

        for letter in s:
           
            if letter == " ":
                continue

            if letter.isdigit():
                num = num * 10 + int(letter)
            else:
                res += (num * sign)
                num = 0
                if letter == "(":
                    stack.append(res)
                    stack.append(sign)
                    res = 0
                    num = 0
                    sign = +1
                elif letter in '+-':
                    num = 0
                    if letter == '+':
                        sign = 1
                    else:
                        sign = -1
                else:
                    num = 0
                    prev_sign = stack.pop()
                    prev_num = stack.pop()
                    res = prev_num + (prev_sign * res)

        res += num * sign           
        return res

                                    
        