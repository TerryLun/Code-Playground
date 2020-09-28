"""
https://app.codility.com/programmers/custom_challenge/palladium2020/
"""


def solution(nums):
    l = len(nums)
    dpl = [0]*(l+1)
    dpr = [0]*(l+1)
    for i in range(l):
        dpl[i+1] = max(nums[i], dpl[i])
    for i in range(l-1, -1, -1):
        dpr[i] = max(nums[i], dpr[i+1])
    r = float('inf')
    for i in range(l+1):
        r = min(r, dpl[i]*i+dpr[i]*(l-i))
    return r
