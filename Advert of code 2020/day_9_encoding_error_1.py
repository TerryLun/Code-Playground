nums = []

while 1:
    line = input()
    if not line:
        break

    nums.append(int(line))

print(nums)


def two_sum(li, target):
    s = set()
    for n in li:
        if n in s:
            return True
        else:
            s.add(target - n)
    return False


for i in range(26, len(nums)):
    curr = nums[i]
    prev = nums[i - 25:i]
    if not two_sum(prev, curr):
        print(curr)
        exit()
