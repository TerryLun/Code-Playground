"""
1232. Check If It Is a Straight Line

You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point.
Check if these points make a straight line in the XY plane.


Constraints:
2 <= coordinates.length <= 1000
coordinates[i].length == 2
-10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
coordinates contains no duplicate point.
"""


def checkStraightLine(coordinates):
    """
    :type coordinates: List[List[int]]
    :rtype: bool
    """
    if len(coordinates) == 1:
        return True

    dy = coordinates[1][1] - coordinates[0][1]
    dx = coordinates[1][0] - coordinates[0][0]

    if dx == 0:  # vertical line
        for i in range(2, len(coordinates)):
            dx = coordinates[i][0] - coordinates[i - 1][0]
            if dx != 0:
                return False
    else:
        slope = dy / dx

        for i in range(2, len(coordinates)):
            dy = coordinates[i][1] - coordinates[i - 1][1]
            dx = coordinates[i][0] - coordinates[i - 1][0]
            if dx == 0 or slope != dy / dx:
                return False

    return True


coordinates = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]
exp = True
print(checkStraightLine(coordinates) == exp)

coordinates = [[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]]
exp = False
print(checkStraightLine(coordinates) == exp)

coordinates = [[1, 1]]
exp = True
print(checkStraightLine(coordinates) == exp)

coordinates = [[1, 1], [2, 2]]
exp = True
print(checkStraightLine(coordinates) == exp)
