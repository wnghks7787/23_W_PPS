a = int(input())
b = int(input())
c = int(input())

x = str(a * b * c)

nums = [0 for i in range(10)]

for num in x:
    nums[int(num)] += 1

for num in nums:
    print(num)