remainder = [0 for i in range(42)]

for i in range(10):
    x = int(input())

    remainder[x % 42] += 1

print(42 - remainder.count(0))