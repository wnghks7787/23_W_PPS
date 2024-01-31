testcase = int(input())

for i in range(testcase):
    k = int(input())
    n = int(input())

    if n == 1:
        print(1)
        continue

    apartment = [[0 for j in range(n)] for l in range(k + 1)]
    
    for j in range(k + 1):
        for l in range(n):
            if j == 0:
                apartment[j][l] = l + 1
            elif l == 0:
                apartment[j][l] = 1
            else:
                apartment[j][l] = apartment[j - 1][l] + apartment[j][l - 1]

    print(apartment[k][n - 1])