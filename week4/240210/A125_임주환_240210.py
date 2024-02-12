n = int(input())

ropes = [0 for _ in range(n)]
answer = 0

for i in range(n):
    ropes[i] = int(input())

ropes_sorted = sorted(ropes, reverse=True)
answer = ropes_sorted[0]

for i in range(n):
    if ropes_sorted[i] * (i + 1) >= answer:
        answer = ropes_sorted[i] * (i + 1)
    else:
        continue

print(answer)