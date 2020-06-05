"""
https://www.hackerrank.com/challenges/bon-appetit/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign
"""


def bonAppetit(bill, k, b):
    b *= 100
    ba = (sum(bill) - bill[k]) * 100 // 2
    if b == ba:
        print('Bon Appetit')
    else:
        print((b - ba) // 100)
