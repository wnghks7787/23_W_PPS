test = int(input())

for i in range(test):
    s = list(map(str, input()))
    answer = 2015
    for j in range(26):
        if s.count(chr(ord('A') + j)) > 0:
            answer -= (ord('A') + j)

    print(answer)