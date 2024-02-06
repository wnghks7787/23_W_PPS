n = int(input())
arr = list(map(int, input().split()))

arr_set = set(arr)
arr = list(arr_set)
arr_sorted = sorted(arr)

print(*arr_sorted)