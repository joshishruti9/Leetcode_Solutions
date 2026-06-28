class Solution:
    def dayOfYear(self, date: str) -> int:

        month_day = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:30}

        date_list = date.split("-")
        val = int(date_list[2])

        month = int(date_list[1])
        year = int(date_list[0])
        
        for i in range(1, month):
            val += month_day[i]
            if i == 2:
                if (year % 100 != 0 and year % 4 == 0) or (year % 100 == 0 and year % 400 == 0):
                    val += 1

        return val
        