n = int(input())

people = []
for i in range(n):
    info = list(map(str, input().split()))
    info[0] = int(info[0])
    people.append(info)

people_sorted = sorted(people, key=lambda x:x[0])

for person in people_sorted:
    print(*person)