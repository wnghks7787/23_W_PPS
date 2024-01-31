room_no = str(input())

nums = [0 for i in range(10)]

for num in room_no:
    if num != '6' and num != '9':
        nums[int(num)] += 1
    else:
        nums[6] += 1

if nums[6] % 2 == 0:
    nums[6] = int(nums[6] / 2)
else:
    nums[6] = int(nums[6] / 2) + 1

print(max(nums))