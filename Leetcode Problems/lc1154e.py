"""
1154. Day of the Year

Given a string date representing a Gregorian calendar date formatted as YYYY-MM-DD, return the day number of the year.

Constraints:
date.length == 10
date[4] == date[7] == '-', and all other date[i]'s are digits
date represents a calendar date between Jan 1st, 1900 and Dec 31, 2019.
"""

class Solution(object):

    def dayOfYear(self, date):
        """
        :type date: str
        :rtype: int
        """
        days_in_year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        year, month, day = date.split('-')
        year, month, day = int(year), int(month), int(day)
        if (year % 4 == 0 or year % 400 == 100) and year % 100 != 0:
            days_in_year[1] = 29

        result = day
        for m in range(month - 1):
            result += days_in_year[m]

        return result


date = "2019-01-09"
exp = 9
s = Solution()
print(s.dayOfYear(date))
print(s.dayOfYear(date) == exp)

date = "2019-02-10"
exp = 41
s = Solution()
print(s.dayOfYear(date))
print(s.dayOfYear(date) == exp)

date = "2003-03-01"
exp = 60
s = Solution()
print(s.dayOfYear(date))
print(s.dayOfYear(date) == exp)

date = "2004-03-01"
exp = 61
s = Solution()
print(s.dayOfYear(date))
print(s.dayOfYear(date) == exp)

date = "1900-03-25"
exp = 84
s = Solution()
print(s.dayOfYear(date))
print(s.dayOfYear(date) == exp)
