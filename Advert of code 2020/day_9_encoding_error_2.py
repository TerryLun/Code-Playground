nums = []

while 1:
    line = input()
    if not line:
        break

    nums.append(int(line))


def two_sum(li, target):
    s = set()
    for n in li:
        if n in s:
            return True
        else:
            s.add(target - n)
    return False


target = None

for i in range(26, len(nums)):
    curr = nums[i]
    prev = nums[i - 25:i]
    if not two_sum(prev, curr):
        target = curr
        break

index = nums.index(target)


def find_nums(li, tar):
    for i in range(1, len(li)):
        li[i] += li[i - 1]
    if tar in li:
        return li.index(tar)


for i in range(index):
    new_list = nums[i:]
    j = find_nums(new_list, target)
    if j:
        res_list = nums[i:i + j + 1]
        print(min(res_list) + max(res_list))
