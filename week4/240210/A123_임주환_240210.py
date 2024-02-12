x = int(input())

arr = [0 for _ in range(x)]

for i in range(x):
    if i == 0:
        arr[i] = 0
        continue
    if i == 1 or i == 2:
        arr[i] = 1
        continue

    current_oper = arr[i - 1]

    if (i + 1) % 2 == 0 and current_oper > arr[int((i + 1) / 2) - 1]:
        current_oper = arr[int((i + 1) / 2) - 1]
    if (i + 1) % 3 == 0 and current_oper > arr[int((i + 1) / 3) - 1]:
        current_oper = arr[int((i + 1) / 3) - 1]

    arr[i] = current_oper + 1

print(arr[-1])