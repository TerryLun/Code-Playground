nums = [6, 13, 1, 15, 2, 0]
end_turn = 30000000

num_dict = {nums[i]: i for i in range(len(nums))}
num_dict.pop(nums[-1])
i = len(nums)

while i != end_turn:
    num = nums[-1]

    if num not in num_dict:
        nums.append(0)
    else:
        nums.append(i - 1 - num_dict[num])
    num_dict[num] = i - 1
    i += 1

print(nums[-1])
