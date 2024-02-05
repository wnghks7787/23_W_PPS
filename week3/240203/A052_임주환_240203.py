n = int(input())

for i in range(n):
    answers = input()
    ox_score = 1
    score = 0

    for answer in answers:
        if answer == 'O':
            score += ox_score
            ox_score += 1
        else:
            ox_score = 1

    print(score)