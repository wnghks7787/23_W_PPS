from collections import deque

N, K = map(int, input().split())

Josephus = deque([i+1 for i in range(N)])

print("<", end="")
while True:
    Josephus.rotate(-K)
    print(Josephus.pop(), end="")

    if len(Josephus) != 0:
        print(", ", end="")
    else:
        break
print(">")