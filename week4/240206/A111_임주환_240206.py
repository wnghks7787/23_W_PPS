test = int(input())

for i in range(test):
    station = int(input())

    people = 0
    for j in range(station):
        people += 0.5
        people *= 2
    print(int(people))