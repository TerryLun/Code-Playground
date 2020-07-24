"""
1431. Kids With the Greatest Number of Candies

Given the array candies and the integer extraCandies, where candies[i] represents the number of candies that the ith kid
has.

For each kid check if there is a way to distribute extraCandies among the kids such that he or she can have the greatest
number of candies among them. Notice that multiple kids can have the greatest number of candies.
"""


def kidsWithCandies(candies, extraCandies):
    max_candies = max(candies)
    return [bool(current_candies + extraCandies >= max_candies) for current_candies in candies]
