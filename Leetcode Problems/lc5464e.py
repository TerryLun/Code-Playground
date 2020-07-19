"""
5464. Water Bottles

Given numBottles full water bottles, you can exchange numExchange empty water bottles for one full water bottle.

The operation of drinking a full water bottle turns it into an empty bottle.

Return the maximum number of water bottles you can drink.
"""


def numWaterBottles(numBottles: int, numExchange: int) -> int:
    tot = 0
    carry = 0
    while numBottles:
        tot += numBottles
        numBottles, carry = divmod(numBottles + carry, numExchange)
    return tot


print(numWaterBottles(9, 3))
print(numWaterBottles(15, 4))
print(numWaterBottles(5, 5))
print(numWaterBottles(2, 3))
