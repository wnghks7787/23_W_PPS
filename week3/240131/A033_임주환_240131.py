max = 0
winner = 0

for i in range(5):
    score = list(map(int, input().split()))

    sum_score = sum(score)

    if max < sum_score:
        max = sum_score
        winner = i + 1

print(winner, max)