n = int(input())

points = []

for i in range(n):
    point = list(map(int, input().split()))
    points.append(point)


for point in sorted(points):
    print(point[0], point[1])