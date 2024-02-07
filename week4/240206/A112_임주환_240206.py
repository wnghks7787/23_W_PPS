N, M = map(int, input().split())

package = 1000
solo = 1000

for i in range(M):
    package_tmp, solo_tmp = map(int, input().split())

    if package >= package_tmp:
        package = package_tmp
    if solo >= solo_tmp:
        solo = solo_tmp

if solo == 0:
    print(0)
else:
    good_consume = int(package / solo)
    money = 0

    if good_consume >= 6:
        money = solo * N
    else:
        money += (package * int(N / 6))
        N -= (int(N / 6) * 6)

        if good_consume >= N:
            money += (N * solo)
        else:
            money += package

    print(money)