viliage = int(input())
dist = list(map(int, input().split()))

dist_sorted = sorted(dist)
dist_sorted = dist_sorted[:-1]

sum = 0
for dist_each in dist_sorted:
    sum += dist_each

print(sum)