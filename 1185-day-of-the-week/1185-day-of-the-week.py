from datetime import date
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
    
        curr_date = date(year, month, day)

        return curr_date.strftime("%A")

