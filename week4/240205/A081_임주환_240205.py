test = int(input())

for i in range(test):
    arr = list(map(int, input().split()))

    arr_sorted = sorted(arr)
    print(arr_sorted[7])