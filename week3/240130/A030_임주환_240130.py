import math

GG = 0
GB = 1
BG = 2
BB = 3

current_good_possibility = 1
current_bad_possibility = 1

next_good_possibility = 1
next_bad_possibility = 1

N, feel = map(int, input().split())

feel_possibility = list(map(float, input().split()))

if feel == 0:
    current_good_possibility = feel_possibility[GG]
    current_bad_possibility = feel_possibility[GB]
else:
    current_good_possibility = feel_possibility[BG]
    current_bad_possibility = feel_possibility[BB]

for i in range(N):
    if i == 0:
        continue
    
    next_good_possibility = current_good_possibility * feel_possibility[GG] + current_bad_possibility * feel_possibility[BG]
    next_bad_possibility = current_good_possibility * feel_possibility[GB] + current_bad_possibility * feel_possibility[BB]

    current_good_possibility = next_good_possibility
    current_bad_possibility = next_bad_possibility

print(math.ceil(current_good_possibility * 1000 - 0.5), math.ceil(current_bad_possibility * 1000 - 0.5))