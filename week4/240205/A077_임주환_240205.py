import copy

scores = []
score = [0 for _ in range(2)]

for i in range(8):
    x = int(input())
    score[0] = x
    score[1] = i + 1

    scores.append(copy.deepcopy(score))

scores_sorted = sorted(scores, reverse=True)
scores_sorted = scores_sorted[:5]

sum_score = 0
scores_index = []
for i in range(len(scores_sorted)):
    sum_score += scores_sorted[i][0]
    scores_index.append(scores_sorted[i][1])

scores_index_sorted = sorted(scores_index)

print(sum_score)
print(*scores_index_sorted)