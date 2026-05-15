from datetime import date
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        ref_date = 1
        ref_mon = "January"
        ref_year = 1971
        ref_day = "Friday"

        curr_date = date(year, month, day)

        return curr_date.strftime("%A")

