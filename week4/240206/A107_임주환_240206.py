start, end = map(int, input().split())

arr = []

count = 0
num = 1
answer = 0
for i in range(1000):
    if count == num:
        count = 0
        num += 1
    
    arr.append(num)
    count += 1

    if i + 1 >= start:
        answer += arr[i]
    
    if i + 1 == end:
        break

print(answer)