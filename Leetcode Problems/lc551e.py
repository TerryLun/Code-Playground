"""
551. Student Attendance Record I

You are given a string representing an attendance record for a student. The record only contains the following three characters:
'A' : Absent.
'L' : Late.
'P' : Present.
A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).

You need to return whether the student could be rewarded according to his attendance record.
"""


def checkRecord(s):
    """
    :type s: str
    :rtype: bool
    """
    con_late = 0
    absent = 0
    for rec in s:
        if rec == 'A':
            absent += 1
            con_late = 0
            if absent == 2:
                return False
        elif rec == 'L':
            con_late += 1
            if con_late == 3:
                return False
        else:
            con_late = 0
    return True


i = "PPALLP"
e = True
print(checkRecord(i) == e)
i = "PPALLL"
e = False
print(checkRecord(i) == e)
i = "LALL"
e = True
print(checkRecord(i) == e)
