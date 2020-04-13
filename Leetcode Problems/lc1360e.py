"""
1360. Number of Days Between Two Dates

Write a program to count the number of days between two dates.
The two dates are given as strings, their format is YYYY-MM-DD as shown in the examples.

Constraints:
The given dates are valid dates between the years 1971 and 2100.
"""


def daysBetweenDates(date1, date2):
    """
    :type date1: str
    :type date2: str
    :rtype: int
    """

    def calc_days(y, m, d):
        days = 0

        # from year
        days += (y - 1970) * 365
        # from leap
        if m > 2:
            days += (y - 1970 + 2) // 4
        else:
            days += (y - 1970 + 1) // 4
        # 2100 is not a leap year since y // 100 == 0
        # note 2000 IS a leap year since y // 400 == 0
        if y >= 2100 and m > 2:
            days -= 1

        # from month
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        for mon in range(1, m):
            days += days_in_month[mon]

        # from day
        days += d

        return days

    y1, m1, d1 = map(int, date1.split('-'))
    y2, m2, d2 = map(int, date2.split('-'))
    return abs(calc_days(y1, m1, d1) - calc_days(y2, m2, d2))


# tests
date1 = "2019-06-29"
date2 = "2019-06-30"
exp = 1
print(daysBetweenDates(date1, date2) == exp)

date1 = "2020-01-15"
date2 = "2019-12-31"
exp = 15
print(daysBetweenDates(date1, date2) == exp)

date1 = "1970-01-01"
date2 = "1972-03-01"
exp = 790
print(daysBetweenDates(date1, date2) == exp)

date1 = "2100-09-22"
date2 = "1991-03-12"
exp = 40006
print(daysBetweenDates(date1, date2) == exp)
