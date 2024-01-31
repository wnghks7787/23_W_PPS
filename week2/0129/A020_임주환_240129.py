STATION = 4

train = 0
train_max = train

for i in range(STATION):
    out_t, in_t = map(int, input().split())

    train -= out_t
    train += in_t

    if train > train_max:
        train_max = train

print(train_max)