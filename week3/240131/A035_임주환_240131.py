testcase = int(input())

for i in range(testcase):
    formula = list(map(str, input().split()))

    x = float(formula[0])

    for i in range(len(formula)):
        if i == 0:
            continue
        elif formula[i] == "@":
            x *= 3
        elif formula[i] == "%":
            x += 5
        elif formula[i] == "#":
            x -= 7

    print("{:.2f}".format(x))