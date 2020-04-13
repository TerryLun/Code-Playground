"""
453. Minimum Moves to Equal Array Elements

Given a non-empty integer array of size n, find the minimum number of moves required to make all array elements equal,
where a move is incrementing n - 1 elements by 1.
"""


def minMoves(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # #TLE
    # count = 0
    # while nums[0] != (sum(nums)/len(nums)):
    #     high_index = nums.index(max(nums))
    #     for i in range(len(nums)):
    #         if i != high_index:
    #             nums[i] += 1
    #     count += 1
    # return count
    """
    let's define sum as the sum of all the numbers, before any moves; minNum as the min number int the list; n is the length of the list;

    After, say m moves, we get all the numbers as x , and we will get the following equation
    
        sum + m * (n - 1) = x * n
     
    and actually,
    
         x = minNum + m
      
    This part may be a little confusing, but @shijungg explained very well. let me explain a little again. it comes from two observations:
    
    the minum number will always be minum until it reachs the final number, because every move, other numbers (besides the max) will be increamented too;
    from above, we can get, the minum number will be incremented in every move. So, if the final number is x, it would be minNum + moves;
    and finally, we will get
    
        sum - minNum * n = m
      
    This is just a math calculation.
    """
    return sum(nums) - min(nums) * len(nums)


# tests
inp = [1, 2, 3]
exp = 3
act = minMoves(inp)
if act == exp:
    print('pass1')
else:
    print(act)

inp = [1, 2]
exp = 1
act = minMoves(inp)
if act == exp:
    print('pass2')
else:
    print(act)

inp = [1, 2, 3, 4]
exp = 6
act = minMoves(inp)
if act == exp:
    print('pass3')
else:
    print(act)

inp = [20]
exp = 0
act = minMoves(inp)
if act == exp:
    print('pass4')
else:
    print(act)

inp = [-100, 0, 100]
exp = 300
act = minMoves(inp)
if act == exp:
    print('pass5')
else:
    print(act)
