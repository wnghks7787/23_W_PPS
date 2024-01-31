def change_open(open_door):
    if open_door == 1:
        open_door -= 1
    else:
        open_door += 1
    return open_door

N = int(input())
open_door = int(input())

if N >= 6:
    print("Love is open door")
else:
    for i in range(N - 1):
        open_door = change_open(open_door)
        print(open_door)