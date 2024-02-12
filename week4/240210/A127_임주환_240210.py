x = int(input())

for j in range(x):
    a, b = map(int, input().split())

    if a >= b:
        a, b = b, a

    LCM = a
    i = 1
    while True:
        if (LCM * i) % b == 0:
            LCM *= i
            break
        else:
            i += 1

    print(LCM)