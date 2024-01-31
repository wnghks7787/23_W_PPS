N = int(input())

plug = 1

for i in range(N):
    plug -= 1
    plug += int(input())

print(plug)