1class Solution:
2    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
3
4
5        total_tax = 0
6        no_taxed = income
7        curr_bracket = 0
8
9        for curr_income, tax_rate in brackets:
10            if no_taxed <= 0:
11                break
12            
13            else:
14                taxable = curr_income-curr_bracket
15                amount = min(no_taxed, taxable)
16                total_tax += ((amount) * (tax_rate / 100))
17                no_taxed -= taxable
18                curr_bracket = curr_income
19
20        
21
22        return total_tax
23
24
25        