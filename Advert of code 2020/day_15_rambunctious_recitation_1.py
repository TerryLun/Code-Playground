nums = [6, 13, 1, 15, 2, 0]
end_turn = 2020
for i in range(len(nums), end_turn):
    done = False
    num = nums[i - 1]
    for j in range(i - 2, -1, -1):
        if num == nums[j]:
            nums.append(i - 1 - j)
            done = True
            break
    if not done:
        nums.append(0)

print(nums[-1])
